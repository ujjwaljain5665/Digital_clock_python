from tkinter import *
import time

ob=Tk()
# ob.config(bg="blue")
def update_clock():
    hours = time.strftime("%I")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    am_or_pm = time.strftime("%p")
    time_text = hours + ":" + minutes + ":" + seconds + " " + am_or_pm
    clock.config(text=time_text)
    clock.after(1000, update_clock)

clock=Label(ob,text="00:00:00",font="helvetica 71 bold",bg="black",fg="yellow")
clock.pack()
update_clock()
ob.mainloop()
