from tkinter import Button, Label
import tkinter as tk

window = tk.Tk()

expression = ""

# hey
def press(num):
    global expression

    expression = expression + str(num)
    equation.set(expression)


def equals():
    global expression
    total = str(eval(expression))

    equation.set(total)

    expression = ""


def delete():
    global expression
    equation.set("")


window.rowconfigure([0, 1, 2, 3, 4, 5], minsize=50)
window.columnconfigure([0, 1, 2, 3], minsize=100)

equation = tk.StringVar()
expression_field = tk.Entry(window, textvariable=equation)
expression_field.grid(row=1, column=1)

label = Label(text="CALCULATOR", bg="black", fg="white")
label.grid(row=0, column=0)

button1 = Button(text="1", bg="red", fg="black", command=lambda: press(1))
button2 = Button(text="2", bg="red", fg="black", command=lambda: press(2))
button3 = Button(text="3", bg="red", fg="black", command=lambda: press(3))
buttonPlus = Button(text="+", bg="red", fg="black", command=lambda: press("+"))

button1.grid(row=2, column=0)
button2.grid(row=2, column=1)
button3.grid(row=2, column=2)
buttonPlus.grid(row=2, column=3)

button4 = Button(text="4", bg="red", fg="black", command=lambda: press(4))
button5 = Button(text="5", bg="red", fg="black", command=lambda: press(5))
button6 = Button(text="6", bg="red", fg="black", command=lambda: press(6))
buttonMinus = Button(text="-", bg="red", fg="black", command=lambda: press("-"))

button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)
buttonMinus.grid(row=3, column=3)

button7 = Button(text="7", bg="red", fg="black", command=lambda: press(7))
button8 = Button(text="8", bg="red", fg="black", command=lambda: press(8))
button9 = Button(text="9", bg="red", fg="black", command=lambda: press(9))
buttonMulti = Button(text="*", bg="red", fg="black", command=lambda: press("*"))

button7.grid(row=4, column=0)
button8.grid(row=4, column=1)
button9.grid(row=4, column=2)
buttonMulti.grid(row=4, column=3)

buttonDel = Button(text="DEL", bg="red", fg="black", command=lambda: delete())
button0 = Button(text="0", bg="red", fg="black", command=lambda: press(0))
buttonEquals = Button(text="=", bg="red", fg="black", command=lambda: equals())
buttonMDivide = Button(text="/", bg="red", fg="black", command=lambda: press("/"))

buttonDel.grid(row=5, column=0)
button0.grid(row=5, column=1)
buttonEquals.grid(row=5, column=2)
buttonMDivide.grid(row=5, column=3)

window.mainloop()
