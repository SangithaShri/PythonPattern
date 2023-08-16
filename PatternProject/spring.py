import turtle
import colorsys
t = turtle.Turtle()
s = turtle.Screen().bgcolor('black')
t.speed(20)
n = 86
h = 5
for i in range(100):
    c = colorsys.hsv_to_rgb(h, 1, 0.6)
    h += 1/n
    t.color(c)
    t.left(1)
    t.fd(1)
    for j in range(1):
        t.right(5)
        t.circle(90)

turtle.done()