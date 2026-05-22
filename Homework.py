import tkinter as tk
from tkinter import messagebox

def convert_length():
    try:
        inches = float(entry_inches.get())
        if inches < 0:
            raise ValueError
        cm = inches * 2.54
        label_result.config(text=f"{cm:g} cm", fg="green")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive number.")
        label_result.config(text="Error", fg="red")

root = tk.Tk()
root.title("Inches to CM Converter")
root.geometry("300x180")
root.resizable(False, False)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)

label_inches = tk.Label(root, text="Inches:")
label_inches.grid(row=0, column=0, padx=10, pady=20, sticky="e")

entry_inches = tk.Entry(root)
entry_inches.grid(row=0, column=1, padx=10, pady=20, sticky="w")

btn_convert = tk.Button(root, text="Convert", command=convert_length, bg="red", fg="white")
btn_convert.grid(row=1, column=0, columnspan=2, pady=10)

label_result = tk.Label(root, text="", font=("Arial", 14, "bold"))
label_result.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()