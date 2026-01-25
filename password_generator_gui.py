import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Warning", "Password length should be at least 4")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")
        return

    use_letters = letters_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()

    characters = ""
    password = []

    if use_letters:
        characters += string.ascii_letters
        password.append(random.choice(string.ascii_letters))
    if use_numbers:
        characters += string.digits
        password.append(random.choice(string.digits))
    if use_symbols:
        characters += string.punctuation
        password.append(random.choice(string.punctuation))

    if not characters:
        messagebox.showerror("Error", "Select at least one character type!")
        return

    while len(password) < length:
        password.append(random.choice(characters))

    random.shuffle(password)
    final_password = "".join(password)

    password_entry.delete(0, tk.END)
    password_entry.insert(0, final_password)

    check_strength(final_password)


def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")


def check_strength(password):
    strength = "Weak"
    if len(password) >= 8:
        strength = "Medium"
    if (any(c.isdigit() for c in password) and
        any(c.isalpha() for c in password) and
        any(c in string.punctuation for c in password) and
        len(password) >= 10):
        strength = "Strong"

    strength_label.config(text=f"Strength: {strength}")


# GUI Window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x400")
root.resizable(False, False)

tk.Label(root, text="Password Length:", font=("Arial", 12)).pack(pady=5)
length_entry = tk.Entry(root, font=("Arial", 12), justify="center")
length_entry.pack()

letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Letters", variable=letters_var).pack()
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack()
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack()

tk.Button(root, text="Generate Password", command=generate_password, bg="purple", fg="white").pack(pady=10)

password_entry = tk.Entry(root, font=("Arial", 12), justify="center", width=25)
password_entry.pack(pady=5)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=5)

strength_label = tk.Label(root, text="Strength: ", font=("Arial", 12, "bold"))
strength_label.pack(pady=10)

root.mainloop()
