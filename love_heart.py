import math
from turtle import *
import time

def heartf(y):
    return 15 * math.sin(y) ** 3

def heartf2(y):
    return 12 * math.cos(y) - 5 * math.cos(2 * y) - 2 * math.cos(3 * y) - math.cos(4 * y)

def draw_heart():
    bgcolor("black")
    color("red")
    speed(0)
    pensize(2)

    for pulse in range(5): 
        clear()
        begin_fill()
        for i in range(300):
            x = heartf(i) * (16 + pulse)  
            y = heartf2(i) * (16 + pulse)
            goto(x, y)
        end_fill()
        time.sleep(0.15)

        clear()
        begin_fill()
        for i in range(300):
            x = heartf(i) * 16
            y = heartf2(i) * 16
            goto(x, y)
        end_fill()
        time.sleep(0.2)

    penup()
    goto(0, -20)
    color("white")
    write("I LOVE YOU", align="center", font=("Arial", 28, "bold"))
    hideturtle()
    done()


while True:
    answer = input(" Do you love me? (yes / no): ").lower()

    if answer == "yes":
        print("I LOVE YOU❤️") 
        draw_heart()     
        break
    else:
        print("Try again 😏 Your answer might change ❤️")
