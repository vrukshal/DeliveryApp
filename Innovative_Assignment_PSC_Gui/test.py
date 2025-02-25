from tkinter import *

application_window = Tk()
application_window.title("Application")

# info_dict = {'City': clicked.get(), 'Address': address_entry.get(1.0, END), 'Zipcode': zipcode_entry.get()}

restaurant = LabelFrame(application_window,padx=10,pady=10)
Label(restaurant,text="abc").pack()
restaurant.grid(row=0,column=0,columnspan=2)

cuisine = LabelFrame(application_window,padx=10,pady=10)
Label(cuisine,text="abc").pack()
cuisine.grid(row=1, column=0,columnspan=2)

cart = LabelFrame(application_window,padx=10,pady=10)
Label(cart,text="abc").pack()
cart.grid(row=0, column=2,rowspan = 4)

application_window.mainloop()