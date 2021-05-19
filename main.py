from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]

    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, password)

    print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning(title="Empty fields", message="You should not leave the fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                print(data)
                data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        website_input.delete(0, END)
        password_input.delete(0, END)
        website_input.focus()


# ---------------------------- UI SETUP ------------------------------- #


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
website_input.focus()
username_input = Entry(width=40)
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(0, "test@email.com")
password_input = Entry(width=21)
password_input.grid(row=3, column=1)


# buttons

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

Add_button = Button(text="Add", width=36, command=save)
Add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
