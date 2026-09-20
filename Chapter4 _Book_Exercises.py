import turtle
import math

def jump(length):
    """Move forward length units without leaving a trail.

    Postcondition: Leaves the pen down.
    """
    penup()
    forward(length)
    pendown()

#4.11.1. Exercise
# Write a function called rectangle that draws a rectangle with given side lengths.

t = turtle.Turtle()

def rectangle(width, height):
    for i in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)

##rectangle(200, 100)

#4.11.2. Exercise
# Write a function called rhombus that draws a rhombus with a given side length and a given interior angle.
# For example, here’s a rhombus with side length 50 and an interior angle of 60 degrees.

def rhombus(side_length, angle):
    static_angle = 180 - angle
    for i in range(2):
        t.forward(side_length)
        t.right(angle)
        t.forward(side_length)
        t.right(static_angle)

###rhombus(80, 60)

# this one took me for ever, for some reason it was only drawing 3 sides.

# 4.11.3. Exercise
# Now write a more general function called parallelogram that draws a quadrilateral with parallel sides.

###def parallelogram(side_1, side_2, angle):
    static_angle = 180 - angle
    t.forward(side_1)
    t.right(angle)
    t.forward(side_2)
    t.right(static_angle)
    t.forward(side_1)
    t.right(angle)
    t.forward(side_2)

# Then rewrite rectangle and rhombus to use parallelogram.

# I am going to call it rectangle_2
def rectangle_2(width, height):
    parallelogram(width, height, 90)

###rectangle_2(100, 200) # Calling rectangle_2

# I am going to call it rhombus_2
def rhombus_2(side_length, angle):
    parallelogram(side_length, side_length, angle)

###rhombus_2(100,60)

#4.11.4. Exercise
# Write an appropriately general set of functions that can draw shapes like this.

def triangle(length, angle):
    for i in range(3):
        t.forward(length)
        t.right(180 - angle)

def draw_pie(length, angle, slices):
    for i in range(slices):
        triangle(length, angle)
        t.right(360 / slices)

###triangle(100,60)
###draw_pie(100, 60, 5 ) #this is as closer as I got :(

# 4.11.5. Exercise
# Write an appropriately general set of functions that can draw flowers like this.
# Hint: Use arc to write a function called petal that draws one flower petal.

def arc(t, radius, angle):
    arc_length = 2 * math.pi * radius * angle / 360
    n = int(arc_length / 3)
    step_length = arc_length / n
    step_angle = angle / n

    for _ in range(n):
        t.forward(step_length)
        t.left(step_angle) # Until here I was fine, then the rest I couldn't figure it out, and I asked help from a chatbot ------------

def petal(t, radius, angle):
    for _ in range(2):
        arc(t, radius, angle)
        t.left(180 - angle)

def flower(t, n_petals, radius, angle):
    for _ in range(n_petals):
        petal(t, radius, angle)
        t.left(360 / n_petals)


###flower(t, n_petals=10, radius=90, angle=90)



# Close the turtle graphics window when clicked -----------------------------------------------------
turtle.exitonclick()

# Overall, I think your solutions are better because they all used the a better used of generalization and encapsulation
# across all the exercises, and I just realized that I did not make use of the docstrings at all.
# I think my code can definetly be improved and be cleaner and reusable.