import turtle as t
import time, random

pluma = t.Pen()
pluma.screen.delay(30)
i = 0
j = 0

while j<6:
    pluma.begin_fill()
    while i<4:
        pluma.forward(30)
        pluma.left(90)
        i+=1
    pluma.end_fill()
    pluma.up()
    j+=1
    pluma.setheading(j*60)
    pluma.forward(30)
    c1 = random.uniform(0, 1)
    c2 = random.uniform(0, 1)
    c3 = random.uniform(0, 1)
    pluma.color(c1, c2, c3)
    i=0
    pluma.down()