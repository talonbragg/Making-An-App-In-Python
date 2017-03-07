# You can learn more @ http://usingpython.com/using-tkinter

import Tkinter as tkinter

window = tkinter.Tk()

lbl = tkinter.Label(window, text="This Is a GUI app", fg="WHITE" bg="BLUE", font=("Helvectica", 15))
entry = tkinter.Entry(window)
btn = tkinter.Button(window, text="Button")


lbl.pack()

window.mainloop()
