from tkinter import *
window = Tk()

def numbr():
    pass


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





calc_1.grid(row=1 , column=0)
calc_2.grid(row=1 , column=1)
calc_3.grid(row=1 , column=2)
calc_4.grid(row=2 , column=0)
calc_5.grid(row=2 , column=1)
calc_6.grid(row=2 , column=2)
calc_7.grid(row=3 , column=0)
calc_8.grid(row=3 , column=1)
calc_9.grid(row=3 , column=2)
calc_0.grid(row=4 , column=1)


window.mainloop()