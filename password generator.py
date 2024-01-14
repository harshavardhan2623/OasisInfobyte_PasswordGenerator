import tkinter as tk
from tkinter import ttk, font
from tkinter import messagebox
import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Password Generator")

        # Font settings
        default_font = font.nametofont("TkDefaultFont")
        default_font.configure(size=11)

        # Variables
        self.password_var = tk.StringVar()
        self.length_var = tk.IntVar(value=12)
        self.uppercase_var = tk.BooleanVar(value=True)
        self.lowercase_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)

        # GUI components
        ttk.Label(root, text="Password Length:").grid(row=0, column=0, pady=5, padx=10)
        ttk.Entry(root, textvariable=self.length_var, width=5).grid(row=0, column=1, pady=5, sticky='w')

        ttk.Checkbutton(root, text="Uppercase", variable=self.uppercase_var).grid(row=1, column=0, sticky='w', padx=10)
        ttk.Checkbutton(root, text="Lowercase", variable=self.lowercase_var).grid(row=2, column=0, sticky='w', padx=10)
        ttk.Checkbutton(root, text="Digits", variable=self.digits_var).grid(row=3, column=0, sticky='w', padx=10)
        ttk.Checkbutton(root, text="Symbols", variable=self.symbols_var).grid(row=4, column=0, sticky='w', padx=10)

        ttk.Button(root, text="Generate Password", command=self.generate_password).grid(row=5, column=0, columnspan=2, pady=10)

        ttk.Entry(root, textvariable=self.password_var, state='readonly', width=40, font=("TkDefaultFont", 12)).grid(row=6, column=0, columnspan=2, pady=5)

        ttk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard).grid(row=7, column=0, columnspan=2, pady=10)

    def generate_password(self):
        if not any([self.uppercase_var.get(), self.lowercase_var.get(), self.digits_var.get(), self.symbols_var.get()]):
            messagebox.showerror("Error", "Select at least one character type.")
            return

        characters = ""
        if self.uppercase_var.get():
            characters += string.ascii_uppercase
        if self.lowercase_var.get():
            characters += string.ascii_lowercase
        if self.digits_var.get():
            characters += string.digits
        if self.symbols_var.get():
            characters += string.punctuation

        length = self.length_var.get()
        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_var.set(password)

    def copy_to_clipboard(self):
        if not self.password_var.get():
            messagebox.showerror("Error", "Generate a password first.")
            return
        pyperclip.copy(self.password_var.get())
        messagebox.showinfo("Success", "Password copied to clipboard.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
