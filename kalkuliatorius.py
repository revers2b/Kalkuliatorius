from tkinter import *
window = Tk()
window.title("Calculator")
window.geometry("320x200")

def numbr():
    pass

def symbol():
    pass

def symbol_sum():
    pass

def close():
    window.destroy()

calc_1 = Button(window, text="1", command=numbr)
calc_2 = Button(window, text="2", command=numbr)
calc_3 = Button(window, text="3", command=numbr)
calc_4 = Button(window, text="4", command=numbr)
calc_5 = Button(window, text="5", command=numbr)
calc_6 = Button(window, text="6", command=numbr)
calc_7 = Button(window, text="7", command=numbr)
calc_8 = Button(window, text="8", command=numbr)
calc_9 = Button(window, text="9", command=numbr)
calc_0 = Button(window, text="0", command=numbr)
sym_plus = Button(window, text="+", command=symbol)
sym_minus = Button(window, text="-", command=symbol)
sym_divide = Button(window, text="/", command=symbol)
sym_multi = Button(window, text="*", command=symbol)
num_sum = Button(window, text="=", command=symbol_sum)
clear = Button(window, text="C", command=symbol)
dot = Button(window, text=".", command=symbol)



calc_1.grid(row=2 , column=0)
calc_2.grid(row=2 , column=1)
calc_3.grid(row=2 , column=2)
calc_4.grid(row=3 , column=0)
calc_5.grid(row=3 , column=1)
calc_6.grid(row=3 , column=2)
calc_7.grid(row=4 , column=0)
calc_8.grid(row=4 , column=1)
calc_9.grid(row=4 , column=2)
calc_0.grid(row=5 , column=1)
sym_plus.grid(row=4, column=3)
sym_minus.grid(row=3, column=3)
sym_divide.grid(row=1, column=3)
sym_multi.grid(row=2, column=3)
num_sum.grid(row=5, column=3)
clear.grid(row=5, column=0)
dot.grid(row=5, column=2)

window.bind("<Escape>", lambda event: close())
window.bind("<Return>", lambda event: symbol_sum())

all_sum = Label(window, text="", bd=1, relief=SUNKEN, anchor=CENTER)
all_sum.grid(row=0, column=1)

window.mainloop()