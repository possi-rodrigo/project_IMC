import tkinter as tk

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        bmi = (weight / (height * height))

        if bmi < 18.5:
            result_label.config(text=f"\n Your BMI is {bmi:.2f}" + "\n \n Considered according to the WHO (World Health Organization) \n as UNDERWEIGHT.")
        elif bmi >= 18.5 and bmi <= 24.999:
            result_label.config(text=f"\n Your BMI is {bmi:.2f}" + "\n \n Considered according to the WHO (World Health Organization) \n as NORMAL WEIGHT.")
        elif bmi >= 25 and bmi <= 29.999:
            result_label.config(text=f"\n Your BMI is {bmi:.2f}" + "\n \n Considered according to the WHO (World Health Organization) \n as OVERWEIGHT.")
        elif bmi >= 30 and bmi <= 34.999:
            result_label.config(text=f"\n Your BMI is {bmi:.2f}" + "\n \n Considered according to the WHO (World Health Organization) \n as OBESITY CLASS I.")
        elif bmi >= 35 and bmi <= 39.999:
            result_label.config(text=f"\n Your BMI is {bmi:.2f}" + "\n \n Considered according to the WHO (World Health Organization) \n as OBESITY CLASS II.")
        else:
            result_label.config(text=f"\n Your BMI is {bmi:.2f}" + "\n \n Considered according to the WHO (World Health Organization) \n as OBESITY CLASS III.")
    except ZeroDivisionError:
        result_label.config(text="Cannot divide by zero, enter valid values.")
    except ValueError:
        result_label.config(text="Enter valid values for height and weight as exemplified.")

window = tk.Tk()
window.title("Calculate Your BMI") # Multiple spaces are used to center the title instead of aligning it to the left.
window.geometry("480x250")
window.resizable(False, False)

label_weight = tk.Label(window, text="Enter your weight in kilograms (E.g.: 12.34)")
label_weight.pack()
weight_entry = tk.Entry(window)
weight_entry.pack()

label_height = tk.Label(window, text="\n Enter your height in meters (E.g.: 1.23)")
label_height.pack()
height_entry = tk.Entry(window)
height_entry.pack()

calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()