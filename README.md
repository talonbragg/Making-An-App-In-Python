# How to Make a GUI App in Python
**This is a tutorial on how to make a basic GUI app in Python.**

The first thing that you need to do when creating a Graphical User Interface in python, is initialize the window. This is how I do it in three lines of code

```python
import Tkinter as tkinter

window = tkinter.Tk()

window.mainloop()
```

Then you should see something like this when you run the python:

<img src="http://usingpython.com/wp-content/uploads/EmptyGUI.jpg">

This is the windo where all of your content is going to go

To change the size of the window, use this code: 

```python
import Tkinter as tkinter

window = tkinter.Tk()

#This line will change the width and the height with the measurement of pixels
window.geometry("500x500")
# ============================================================================

window.mainloop()

```

Now when you run this, the window should be a little bit bigger.

Now, lets customize this empty window, You probably want to add a window title and your icon, well, Tkinter makes that fairly easy. The code that you add will have a comment above it:

```python
import Tkinter as tkinter

window = tkinter.Tk()

# These two lines will help you customize the window a little bit more
window.title("Super-Cool Window")
window.wm_iconbitmap("youriconhere.ico")
# ====================================================================

window.geometry("500x500")

window.mainloop()
```
This is what my window looks like:

<img src="http://usingpython.com/wp-content/uploads/SuperCoolWindow.jpg">

Now we might want to add some text to this, it would make it have a little bit more of a purpose.

```python
import Tkinter as tkinter

window = tkinter.Tk()


window.title("Super-Cool Window")
window.wm_iconbitmap("youriconhere.ico")

# This is what you want to add, it is a label
lbl = tkinter.Label(window, text="This is a nice label")
=============================================

window.geometry("500x500")

window.mainloop()
```
Now, try this on your own to see what happens.

**===================================================================**

**Thank You For Reading This Tutorial**

**Be sure to checkout the example code [HERE](https://github.com/talonbragg/Making-An-App-In-Python/blob/master/example.py).**

**You can learn more [HERE](http://usingpython.com/using-tkinter/).**

**Photo credits to http://usingpython.com**

**===================================================================**
