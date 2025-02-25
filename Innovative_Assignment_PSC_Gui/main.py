import sqlite3
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Login Page")


# root.geometry("400x400")

def application():

    info_dict = {'City': clicked.get(), 'Address': address_entry.get(1.0, END), 'Zipcode': zipcode_entry.get()}

    info_window.destroy()
    application_window = Tk()
    application_window.title("Application")

    restaurant = LabelFrame(application_window, padx=10, pady=10)
    Label(restaurant, text="abc").pack()
    restaurant.grid(row=0, column=0, columnspan=2)

    cuisine = LabelFrame(application_window, padx=10, pady=10)
    Label(cuisine, text="abc").pack()
    cuisine.grid(row=1, column=0, columnspan=2)

    cart = LabelFrame(application_window, padx=10, pady=20)
    Label(cart, text="abc").pack()
    cart.grid(row=0, column=2, rowspan=2)

    application_window.mainloop()


def info():
    global info_window
    info_window = Tk()
    info_window.title("Delivery Information")

    global clicked
    global address_entry
    global zipcode_entry

    def address_clear(event):
        address_entry.delete(1.0, "end")

    def zipcode_clear(event):
        zipcode_entry.delete(0, "end")

    def check_entries():
        if clicked.get() == "City":
            messagebox.showerror("error nme", "choose a city")
        elif address_entry.get(1.0, END).strip() == "Address" or address_entry.get(1.0, END).strip() == "":
            messagebox.showerror("error", "enter your address")
        elif (zipcode_entry.get()).isnumeric() == FALSE or len(zipcode_entry.get()) != 6 or zipcode_entry.get() == "":
            messagebox.showerror("error", "enter a valid zipcode")
        else:
            application()

    cities = ["City", "Ahmedabad", "Mumbai", "Delhi", "Bengaluru", "Rajkot", "Surat", "Chennai", "Pune", "Kolkata",
              "Vadodara", "Valsad"]
    clicked = StringVar()
    clicked.set(cities[0])
    drop = OptionMenu(info_window, clicked, *cities)
    drop.grid(row=0, column=1)
    city_label = Label(info_window, text="City")
    city_label.grid(row=0, column=0)

    address_label = Label(info_window, text="Address")
    address_label.grid(row=1, column=0)
    address_entry = Text(info_window)
    address_entry.insert(1.0, "Address")
    address_entry.bind("<Button-1>", address_clear)
    address_entry.grid(row=1, column=1, columnspan=2)

    zipcode_label = Label(info_window, text="Zipcode")
    zipcode_label.grid(row=2, column=0)
    zipcode_entry = Entry(info_window)
    zipcode_entry.insert(0, "Zipcode")
    zipcode_entry.bind("<Button-1>", zipcode_clear)
    zipcode_entry.grid(row=2, column=1)

    next = Button(info_window, text="next", command=check_entries)
    next.grid(row=4, column=0, columnspan=2)

    info_window.mainloop()


def check_in_database():
    conn = sqlite3.connect('data.db')

    c = conn.cursor()

    if email_entry.get() == "":
        messagebox.showerror("Login status", "Email Empty")
    elif password_entry.get() == "":
        messagebox.showerror("Login status", "Password Empty")
    else:
        password = c.execute("select email,password from Customer_Info")
        password = password.fetchall()
        temp1 = (email_entry.get(), password_entry.get())

        if password.__contains__(temp1):
            messagebox.showinfo("Login status", "Logged in successfully")
            root.destroy()
            sign_in_window.destroy()
            info()
        else:
            messagebox.showerror("Login status", "Invalid username or password")

    conn.commit()

    conn.close()


def add_to_database():
    conn = sqlite3.connect('data.db')

    c = conn.cursor()

    # c.execute("""CREATE TABLE Customer_Info(
    #     first_name text,
    #     last_name text,
    #     email text,
    #     password text
    #                 )""")

    if first_name_entry_up.get() == "":
        messagebox.showerror("Account Status", "First Name Empty")
    elif last_name_entry_up.get() == "":
        messagebox.showerror("Account Status", "Last Name Empty")
    elif email_entry_up.get() == "":
        messagebox.showerror("Account Status", "Email Empty")
    elif password_entry_up.get() == "":
        messagebox.showerror("Account Status", "Password Empty")
    else:
        email = str(email_entry_up.get())
        temp = (email,)
        all_email = c.execute("select email from Customer_Info")
        all_email = all_email.fetchall()

        if email.__contains__("@"):
            if all_email.__contains__(temp):
                messagebox.showerror("Account Status", "Email already exists.\nEnter a new one.")
            else:
                c.execute(
                    "insert into Customer_Info values (:first_name_entry_up,:last_name_entry_up,:email_entry_up,"
                    ":password_entry_up)",
                    {
                        'first_name_entry_up': first_name_entry_up.get(),
                        'last_name_entry_up': last_name_entry_up.get(),
                        'email_entry_up': email_entry_up.get(),
                        'password_entry_up': password_entry_up.get()
                    }
                )
                messagebox.showinfo("Account Status", "Account Created")
                sign_up_window.destroy()

        else:
            messagebox.showerror("Account Status", "Enter a valid Email.")
    conn.commit()

    conn.close()


def sign_in_fun():
    # global sign_in_button
    # sign_in_button.grid_forget()

    global password_entry
    global email_entry
    global sign_in_window

    sign_in_window = Tk()

    def email_clear(event):
        email_entry.delete(0, "end")

    sign_in = LabelFrame(sign_in_window, text="Sign in", padx=5, pady=5)
    sign_in.grid(row=0, column=0)

    email = Label(sign_in, text="Email")
    email.grid(row=0, column=0, sticky=W, padx=7)
    email_entry = Entry(sign_in)
    email_entry.insert(0, "Email")
    email_entry.bind("<Button-1>", email_clear)
    email_entry.grid(row=0, column=1)

    password = Label(sign_in, text="Password")
    password.grid(row=1, column=0, sticky=W, padx=7)
    password_entry = Entry(sign_in, show="*")
    password_entry.grid(row=1, column=1)

    login_button = Button(sign_in, text="Login", command=check_in_database)
    login_button.grid(row=2, column=0, columnspan=2)
    sign_in_window.mainloop()


def sign_up_fun():
    # global sign_up_button
    # sign_up_button.grid_forget()

    global first_name_entry_up
    global last_name_entry_up
    global email_entry_up
    global password_entry_up
    global sign_up_window

    def email_clear(event):
        email_entry_up.delete(0, "end")

    def first_clear(event):
        first_name_entry_up.delete(0, "end")

    def last_clear(event):
        last_name_entry_up.delete(0, "end")

    sign_up_window = Toplevel(root)

    sign_up = LabelFrame(sign_up_window, text="Sign up", padx=5, pady=5)
    sign_up.grid(row=1, column=0)

    first_name_up = Label(sign_up, text="First name")
    first_name_up.grid(row=0, column=0, sticky=W, padx=7)
    first_name_entry_up = Entry(sign_up)
    first_name_entry_up.insert(0, "First_name")
    first_name_entry_up.bind("<Button-1>", first_clear)
    first_name_entry_up.grid(row=0, column=1)

    last_name_up = Label(sign_up, text="Last name")
    last_name_up.grid(row=1, column=0, sticky=W, padx=7)
    last_name_entry_up = Entry(sign_up)
    last_name_entry_up.insert(0, "Last Name")
    last_name_entry_up.bind("<Button-1>", last_clear)
    last_name_entry_up.grid(row=1, column=1)

    email_up = Label(sign_up, text="Email")
    email_up.grid(row=2, column=0, sticky=W, padx=7)
    email_entry_up = Entry(sign_up)
    email_entry_up.insert(0, "Email")
    email_entry_up.bind("<Button-1>", email_clear)
    email_entry_up.grid(row=2, column=1)

    password_up = Label(sign_up, text="Password")
    password_up.grid(row=3, column=0, sticky=W, padx=7)
    password_entry_up = Entry(sign_up, show="*")
    password_entry_up.grid(row=3, column=1)

    sign_up_button = Button(sign_up, text="Create account", command=add_to_database)
    sign_up_button.grid(row=4, column=0, columnspan=2)

    # sign_up_window.mainloop()


sign_in_button = Button(root, text="Sign in", padx=10, pady=10, command=sign_in_fun)
sign_in_button.grid(row=0, column=0)

sign_up_button = Button(root, text="Sign up", padx=10, pady=10, command=sign_up_fun)
sign_up_button.grid(row=1, column=0)

root.mainloop()
