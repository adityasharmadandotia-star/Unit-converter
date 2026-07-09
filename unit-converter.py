import tkinter as tk
from tkinter import ttk, messagebox

# -------------------- Conversion Data --------------------

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

# -------------------- Functions --------------------

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

# -------------------- Window --------------------

root = tk.Tk()
root.title("Unit Converter")
root.geometry("500x600")
root.configure(bg="#1E1E2E")
root.resizable(False, False)

# -------------------- Title --------------------

title = tk.Label(
    root,
    text="⚡ Unit Converter",
    font=("Segoe UI", 24, "bold"),
    bg="#1E1E2E",
    fg="white"
)
title.pack(pady=20)

# -------------------- Category --------------------

tk.Label(
    root,
    text="Category",
    bg="#1E1E2E",
    fg="white",
    font=("Segoe UI",11,"bold")
).pack()

category_var = tk.StringVar(value="Length")

category_box = ttk.Combobox(
    root,
    textvariable=category_var,
    values=["Length","Weight","Temperature"],
    state="readonly",
    width=28
)
category_box.pack(pady=5)
category_box.bind("<<ComboboxSelected>>", update_units)

# -------------------- Value --------------------

tk.Label(
    root,
    text="Value",
    bg="#1E1E2E",
    fg="white",
    font=("Segoe UI",11,"bold")
).pack(pady=(10,5))

value_entry = tk.Entry(
    root,
    width=30,
    font=("Segoe UI",12),
    justify="center"
)
value_entry.pack()

# -------------------- From --------------------

tk.Label(
    root,
    text="From",
    bg="#1E1E2E",
    fg="white",
    font=("Segoe UI",11,"bold")
).pack(pady=(10,5))

from_var = tk.StringVar()

from_box = ttk.Combobox(
    root,
    textvariable=from_var,
    state="readonly",
    width=28
)
from_box.pack()

# -------------------- To --------------------

tk.Label(
    root,
    text="To",
    bg="#1E1E2E",
    fg="white",
    font=("Segoe UI",11,"bold")
).pack(pady=(10,5))

to_var = tk.StringVar()

to_box = ttk.Combobox(
    root,
    textvariable=to_var,
    state="readonly",
    width=28
)
to_box.pack()

# -------------------- Button --------------------

convert_btn = tk.Button(
    root,
    text="⚡ Convert",
    command=convert,
    bg="#6C63FF",
    fg="white",
    activebackground="#4F46E5",
    activeforeground="white",
    font=("Segoe UI",12,"bold"),
    bd=0,
    padx=20,
    pady=10,
    cursor="hand2"
)
convert_btn.pack(pady=25)

convert_btn.bind(
    "<Enter>",
    lambda e: convert_btn.config(bg="#4F46E5")
)

convert_btn.bind(
    "<Leave>",
    lambda e: convert_btn.config(bg="#6C63FF")
)

# -------------------- Result --------------------

result_label = tk.Label(
    root,
    text="Result",
    bg="#2A2A40",
    fg="#00E676",
    font=("Segoe UI",18,"bold"),
    width=22,
    height=2
)
result_label.pack()

update_units()

root.mainloop()

