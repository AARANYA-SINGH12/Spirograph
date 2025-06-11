import turtle as t
import random

t.colormode(255)
def random_colours():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colour_rgb = (r , g ,b)
    return colour_rgb

tim = t.Turtle()
tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tim.color(random_colours())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()