# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

FONT = ("Arial", 14, "normal")

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

# image canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# labels

website_label = Label(text="Website:", font=FONT)
website_label.grid(row=1, column=0)
username_label = Label(text="Email/Username:", font=FONT)
username_label.grid(row=2, column=0)
password_label = Label(text="Password:", font=FONT)
password_label.grid(row=3, column=0)

# entries

website_input = Entry(width=40)
website_input.grid(row=1, column=1, columnspan=2)
username_input = Entry(width=40)
username_input.grid(row=2, column=1, columnspan=2)
password_input = Entry(width=21)
password_input.grid(row=3, column=1)


# buttons

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)

Add_button = Button(text="Add", width=36)
Add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
