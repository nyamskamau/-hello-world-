from turtle import *
from tkinter import *
def circ():
    color("black")
    begin_fill()
    write(circle(rad,speed(5)))
    end_fill()
    left(-15)
    
    write(circle(rad/2,180))
    color("blue")
    begin_fill()
    write(circle(rad/2,180))
    end_fill()
    color("black")
    begin_fill()
    write(circle(-rad,36))
    write(circle(-rad,108))
    end_fill()
rad=int(input('enter radius: '))
for i in range(1,10):
    circ()
