import tkinter as tk
from tkinter import ttk, messagebox

# Conversion Data
length = {
    "Meter": 1,
    "Kilometer": 1000,
    "Centimeter": 0.01,
    "Millimeter": 0.001
}

weight = {
    "Kilogram": 1,
    "Gram": 0.001,
    "Pound": 0.453592
}

def update_units(event=None):
    category = category_var.get()

    if category == "Length":
        units = list(length.keys())
    elif category == "Weight":
        units = list(weight.keys())
    else:
        units = ["Celsius", "Fahrenheit", "Kelvin"]

    from_box["values"] = units
    to_box["values"] = units
    from_box.current(0)
    to_box.current(1 if len(units) > 1 else 0)

def convert():
    try:
        value = float(value_entry.get())
        category = category_var.get()
        from_unit = from_var.get()
        to_unit = to_var.get()

        if category == "Length":
            result = value * length[from_unit] / length[to_unit]

        elif category == "Weight":
            result = value * weight[from_unit] / weight[to_unit]

        else:
            # Temperature
            if from_unit == "Celsius":
                c = value
            elif from_unit == "Fahrenheit":
                c = (value - 32) * 5 / 9
            else:
                c = value - 273.15

            if to_unit == "Celsius":
                result = c
            elif to_unit == "Fahrenheit":
                result = c * 9 / 5 + 32
            else:
                result = c + 273.15

        result_label.config(text=f"{result:.4f} {to_unit}")

    except:
        messagebox.showerror("Error", "Enter a valid number")

# Window
root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x350")
root.resizable(False, False)

title = tk.Label(root, text="Unit Converter",
                 font=("Arial", 18, "bold"))
title.pack(pady=10)

# Category
tk.Label(root, text="Category").pack()

category_var = tk.StringVar(value="Length")

category_box = ttk.Combobox(
    root,
    textvariable=category_var,
    values=["Length", "Weight", "Temperature"],
    state="readonly"
)

category_box.pack()
category_box.bind("<<ComboboxSelected>>", update_units)

# Value
tk.Label(root, text="Value").pack(pady=5)

value_entry = tk.Entry(root, width=25)
value_entry.pack()

# From
tk.Label(root, text="From").pack(pady=5)

from_var = tk.StringVar()
from_box = ttk.Combobox(root,
                        textvariable=from_var,
                        state="readonly")
from_box.pack()

# To
tk.Label(root, text="To").pack(pady=5)

to_var = tk.StringVar()
to_box = ttk.Combobox(root,
                      textvariable=to_var,
                      state="readonly")
to_box.pack()

# Button
convert_btn = tk.Button(root,
                        text="Convert",
                        command=convert,
                        bg="blue",
                        fg="white",
                        width=20)

convert_btn.pack(pady=15)

# Result
result_label = tk.Label(root,
                        text="Result",
                        font=("Arial", 14, "bold"))

result_label.pack()

update_units()

root.mainloop()
