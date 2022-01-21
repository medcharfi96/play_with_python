#!/usr/bin/env python3

from os import lseek
import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen().bgcolor("black")
t.color("white")
t.speed(0)
t.width(8)
n = 66
h = 0
for count in range(5):
    t.right(144)
    for c in range(n):
        t.forward(3)
        c = colorsys.hsv_to_rgb(8,1,1)
        h +=1/n
        t.color(c)
turtle.exitonclick()