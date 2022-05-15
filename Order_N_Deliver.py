"""
Program Name: Order N Deliver
Author: Tyke Anfield
Last Update 5/14/2022
Purpose: Gui to simulate a pizza ordering app
"""


from tkinter import *
import sqlite3
from PIL import ImageTk, Image

# First window
root = Tk()
root.title("Order N Deliver")
root.geometry('450x400+600+300')


# Frames to separate first window
top_frame = Frame(root, height=200, width=450)
top_frame.place(x=0, y=0)
bot_frame = Frame(root, height=200, width=450)
bot_frame.place(x=0, y=120)

# Label first window
win_title = Label(top_frame, text="Customer Info")
win_title.place(x=170, y=40)

# button to select delivery
b_delivery = Button(top_frame, text='Delivery', padx=30, command=lambda: Click_Delivery())
b_delivery.place(x=95, y=80)

# button to select carryout
b_carryout = Button(top_frame, text="Carry Out", padx=30, command=lambda: click_carryout())
b_carryout.place(x=220, y=80)


# Button to exit program
btn_quit = Button(top_frame, text='Exit Program', command=lambda: root.quit())
btn_quit.place(x=10, y=10)


# ===============================================Ordering_Screen========================================================

# Function to open second window for ordering
def OrderingScreen():
    global Pepperoni
    global supreme_pizza
    global meats
    global veggie
    global buff_chicken
    global taco_pizza

    # Window to take and output order total
    order_screen = Toplevel()
    order_screen.title("Order menu")
    order_screen.geometry('600x600+425+125')

    # frames to split window
    top_frame2 = Frame(order_screen, height=100, width=600, bg="green")
    top_frame2.place(x=0, y=0)
    left_frame = Frame(order_screen, height=400, width=600, bg="light gray")
    left_frame.place(x=0, y=100)
    right_frame = Frame(order_screen, height=100, width=600, bg="red")
    right_frame.place(x=0, y=500)

    # Title for frames
    order_title = Label(top_frame2, text="Order For: ", font='SERIF')
    order_title.place(x=150, y=15)
    order_left = Label(left_frame, text="Specialty Pizzas", font='SERIF')
    order_left.place(x=230, y=0)
    order_right = Label(right_frame, text="Total purchase:   $", font='SERIF')
    order_right.place(x=105, y=5)

    # Gets customer info from first window and displays it order_title
    f_name_label = Label(top_frame2, text="First name: " + f_name.get(), font=('SERIF', 12))
    f_name_label.place(x=262, y=10)
    l_name_label = Label(top_frame2, text="Last name: " + l_name.get(), font=('SERIF', 12))
    l_name_label.place(x=262, y=40)
    phone_label = Label(top_frame2, text="Phone Number: " + phone.get(), font=('SERIF', 12))
    phone_label.place(x=262, y=70)

    # Pizza Images
    Pepperoni = ImageTk.PhotoImage(Image.open("Images/Pepperoni_Pizza.png"))
    img_label = Label(left_frame, image=Pepperoni)
    img_label.place(x=75, y=105)
    supreme_pizza = ImageTk.PhotoImage(Image.open("Images/Supreme_Pizza.png"))
    img_label = Label(left_frame, image=supreme_pizza)
    img_label.place(x=250, y=105)
    meats = ImageTk.PhotoImage(Image.open("Images/Meats _Pizza.png"))
    img_label = Label(left_frame, image=meats)
    img_label.place(x=465, y=105)
    veggie = ImageTk.PhotoImage(Image.open("Images/Viggie_Pizza.bmp"))
    img_label = Label(left_frame, image=veggie)
    img_label.place(x=75, y=295)
    buff_chicken = ImageTk.PhotoImage(Image.open("Images/Buffalo_Chicken_Pizza.png"))
    img_label = Label(left_frame, image=buff_chicken)
    img_label.place(x=250, y=295)
    taco_pizza = ImageTk.PhotoImage(Image.open("Images/Taco_Pizza.bmp"))
    img_label = Label(left_frame, image=taco_pizza)
    img_label.place(x=465, y=295)

    # pizza Labels
    pepperoni_title = Label(left_frame, text="Pepperoni Pizza: $8", font='SERIF')
    pepperoni_title.place(x=5, y=65)
    supreme_pizza_title = Label(left_frame, text="Supreme Pizza: $12", font='SERIF')
    supreme_pizza_title.place(x=205, y=65)
    meats_title = Label(left_frame, text="Meats Pizza: $12", font='SERIF')
    meats_title.place(x=425, y=65)
    veggie_title = Label(left_frame, text="Veggie Pizza: $10", font='SERIF')
    veggie_title.place(x=5, y=250)
    buff_chicken_title = Label(left_frame, text="Buffalo Chicken Pizza: $12", font='SERIF')
    buff_chicken_title.place(x=185, y=250)
    taco_pizza_title = Label(left_frame, text="Taco Pizza: $10", font='SERIF')
    taco_pizza_title.place(x=455, y=250)

    # Add Pizzas
    pep_spin = Spinbox(left_frame, from_=0, to=999)
    pep_spin.place(x=45, y=165)
    supreme_spin = Spinbox(left_frame, from_=0, to=999)
    supreme_spin.place(x=230, y=165)
    meats_spin = Spinbox(left_frame, from_=0, to=999)
    meats_spin.place(x=440, y=165)
    veggie_spin = Spinbox(left_frame, from_=0, to=999)
    veggie_spin.place(x=45, y=365)
    buff_chicken_spin = Spinbox(left_frame, from_=0, to=999)
    buff_chicken_spin.place(x=230, y=365)
    taco_spin = Spinbox(left_frame, from_=0, to=999)
    taco_spin.place(x=440, y=365)

    # Function to add or subtract pizzas using spinboxes
    def add_pizza():
        pepPizza = pep_spin.get()
        supremePizza = supreme_spin.get()
        meatsPizza = meats_spin.get()
        veggiePizza = veggie_spin.get()
        buffChickenPizza = buff_chicken_spin.get()
        tacoPizza = taco_spin.get()
        total = (int(pepPizza) * 8) \
                + (int(supremePizza) * 12) \
                + (int(meatsPizza) * 12) \
                + (int(veggiePizza) * 10) \
                + (int(buffChickenPizza) * 12) \
                + (int(tacoPizza) * 10)

        total = Label(right_frame, text=total, font='SERIF')
        total.place(x=340, y=5)

        # Resets Total
        butn = Button(right_frame, text='Reset Total', font='SERIF', command=lambda: total.destroy())
        butn.place(x=425, y=40)

    # button to confirm pizza choices
    btnn = Button(right_frame, text='submit', font='SERIF', command=lambda: add_pizza())
    btnn.place(x=255, y=40)

    # Quit button
    btn_quit2 = Button(top_frame2, text='Exit Program', command=lambda: root.quit())
    btn_quit2.place(x=10, y=10)
    # Close Order screen
    back_btn = Button(top_frame2, text='Back to first screen', command=lambda: order_screen.destroy())
    back_btn.place(x=10, y=50)


# =================================================Order_Database=======================================================

# Database for customer information
conn = sqlite3.connect('address_book.db')

# Create cursor
c = conn.cursor()

# Create table
'''
c.execute("""CREATE TABLE addresses(
        first_name text, 
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer,
        phone_number integer
        )""")
'''


# Function submits the entered delivery and/or carryout information to the database
def click_submit():


    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    # Insert into Table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode, :phone)",
                   {
                       'f_name': f_name.get(),
                       'l_name': l_name.get(),
                       'address': address.get(),
                       'city': city.get(),
                       'state': state.get(),
                       'zipcode': zipcode.get(),
                       'phone': phone.get()
                   })

    # Commit Changes
    conn.commit()

    # Close Connections
    conn.close()

    # Clear the Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)
    phone.delete(0, END)

# Function when delivery button is clicked opens entry widgets and labels to type in customer information
# also opens a button to "continue to next screen" to open the next window,
# and a reset button to close all widgets and labels
def Click_Delivery():
    global f_name
    global l_name
    global address
    global city
    global state
    global zipcode
    global phone
    global f_name_label
    global l_name_label
    global address_label
    global city_label
    global state_label
    global  zipcode_label
    global phone_label
    global b_submit
    global reset_btn
    global query_btn
# Create text boxes
    f_name = Entry(bot_frame, width=30)
    f_name.grid(row=0, column=1)
    l_name = Entry(bot_frame, width=30)
    l_name.grid(row=1, column=1)
    phone = Entry(bot_frame, width=30)
    phone.grid(row=2, column=1)
    address = Entry(bot_frame, width=30)
    address.grid(row=3, column=1)
    city = Entry(bot_frame, width=30)
    city.grid(row=4, column=1)
    state = Entry(bot_frame, width=30)
    state.grid(row=5, column=1)
    zipcode = Entry(bot_frame, width=30)
    zipcode.grid(row=6, column=1)


    # Create Text Box Labels
    f_name_label = Label(bot_frame, text="Enter first name")
    f_name_label.grid(row=0, column=0)
    l_name_label = Label(bot_frame, text="Enter last name")
    l_name_label.grid(row=1, column=0)
    phone_label = Label(bot_frame, text="Enter phone number")
    phone_label.grid(row=2, column=0)
    address_label = Label(bot_frame, text="Enter address")
    address_label.grid(row=3, column=0)
    city_label = Label(bot_frame, text="Enter city")
    city_label.grid(row=4, column=0)
    state_label = Label(bot_frame, text="Enter state")
    state_label.grid(row=5, column=0)
    zipcode_label = Label(bot_frame, text="Enter zipcode")
    zipcode_label.grid(row=6, column=0)


    # Create Submit button
    b_submit = Button(bot_frame, text='submit info', command=lambda: click_submit())
    b_submit.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    query_btn = Button(bot_frame, text='Continue to next screen', command=lambda: OrderingScreen())
    query_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

    reset_btn = Button(bot_frame, text="reset window", command=lambda: reset())
    reset_btn.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=137)


# Function when carryout button is clicked opens entry widgets and labels to type in customer information
# also opens a button to"continue to next screen" to open the next window,
# and a reset button to close all widgets and labels
def click_carryout():
    global f_name
    global l_name
    global phone
    global f_name_label
    global l_name_label
    global phone_label
    global b_submit
    global btn
    global reset_btn2
    global address
    global city
    global state
    global zipcode
    global phone
    global b_submit
    global reset_btn
    global query_btn
    # Create text boxes
    f_name = Entry(bot_frame, width=30)
    f_name.grid(row=0, column=1)
    l_name = Entry(bot_frame, width=30)
    l_name.grid(row=1, column=1)
    phone = Entry(bot_frame, width=30)
    phone.grid(row=2, column=1)
    address = Entry(bot_frame, width=30)
# place holder entry box to be used in carrout for the database, but not used
    city = Entry(bot_frame, width=30)
# place holder entry box to be used in carrout for the database, but not used
    state = Entry(bot_frame, width=30)
# place holder entry box to be used in carrout for the database, but not used
    zipcode = Entry(bot_frame, width=30)

    # Create Text Box Labels
    f_name_label = Label(bot_frame, text="Enter first name")
    f_name_label.grid(row=0, column=0)
    l_name_label = Label(bot_frame, text="Enter last name")
    l_name_label.grid(row=1, column=0)
    phone_label = Label(bot_frame, text="Enter phone number")
    phone_label.grid(row=2, column=0)


    b_submit = Button(bot_frame, text='submit info', command=lambda: click_submit())
    b_submit.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    btn = Button(bot_frame, text='Continue to next screen', command=lambda: OrderingScreen())
    btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

    reset_btn2 = Button(bot_frame, text="reset window", command=lambda: reset2())
    reset_btn2.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=137)


# reset button funtion to destroy(close) all labels and entry boxes for delivery
def reset():
    f_name.destroy()
    l_name.destroy()
    address.destroy()
    city.destroy()
    state.destroy()
    zipcode.destroy()
    phone.destroy()
    f_name_label.destroy()
    l_name_label.destroy()
    address_label.destroy()
    city_label.destroy()
    state_label.destroy()
    zipcode_label.destroy()
    phone_label.destroy()
    b_submit.destroy()
    query_btn.destroy()
    reset_btn.destroy()


# reset button function to destroy(close) all labels and entry boxes for carryout
def reset2():
    f_name.destroy()
    l_name.destroy()
    phone.destroy()
    f_name_label.destroy()
    l_name_label.destroy()
    phone_label.destroy()
    b_submit.destroy()
    btn.destroy()
    reset_btn2.destroy()

# Commit Changes to database
conn.commit()

# Close Connections to database
conn.close()

# ======================================if __name__ == "__main__":======================================================

if __name__ == "__main__":
    mainloop()
