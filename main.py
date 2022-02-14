from tkinter import *


def calculate():
    miles_number = int(miles_input.get())
    result_label.config(text=round(miles_number * 1.6))


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.focus()
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles", padx=10)
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to", padx=10)
equal_label.grid(column=0, row=1)

result_label = Label(text="0", pady=10)
result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

window.mainloop()
