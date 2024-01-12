# import colorgram

import turtle as t  #we have to change the actual turtle Module, not the object
import random
from turtle import Screen


# Extract 6 colors from an image.
# TODO 1: Extraction is done. No need for the computational code above the #hashtags# below. Comment out below:

# TODO 2: Project stats: Dots should be size 20

# TODO 3: Project stats: Dots should be spaced apart by 50 paces

# TODO 4: Generate a random color from the 6 we will start with

# TODO 5: Draw forward 10 dots, reset, move up 50 paces, draw another 10, repeat until 10 rows and 10 columns are drawn

# colors = colorgram.extract('image.jpg', 10)

# Iterate through all 6 colors and access their RGB values.
# for color in colors:
#     rgb = color.rgb
#     r, g, b = rgb
#     print(f"RGB: ({r}, {g}, {b})")
#################################################################################

color_list = [
    (141, 174, 201),
    (22, 30, 46),
    (34, 106, 151),
    (207, 159, 112),
    (227, 211, 100),
    (141, 28, 61)
]

tod = t.Turtle()
t.colormode(255)
tod.speed("normal")
tod.penup()

tod.setheading(-90)
tod.forward(200)
tod.setheading(-90)
tod.forward(100)
tod.setheading(-270)
tod.forward(100)

tod.setheading(180)
tod.forward(200)
tod.setheading(180)

counter = 0

def draw_rows_to_right():
    # def column_loop():
    for going_right_row in range(1, 11):
        tod.backward(50)
        global random_extracted_color
        random_extracted_color = random.choice(color_list)
        tod.dot(20, random_extracted_color)

            #turn up, then move 1:
    tod.setheading(-90)
    tod.left(90)
    tod.forward(50)
    tod.left(90)
    tod.forward(50)
    tod.left(90)
    for going_right_row in range(1, 11):
        tod.forward(50)
        random_extracted_color = random.choice(color_list)
        tod.dot(20, random_extracted_color)
    tod.left(90)
    tod.backward(50)
    tod.right(90)
    tod.forward(50)
    draw_rows_to_right()




            # for going_right_row in range(1, 9):
            #     tod.backward(50)
            #     random_extracted_color = random.choice(color_list)
            #     tod.dot(20, random_extracted_color)


            #turn left, then move 9 more spaces,

            #turn up, move 1:

            #turn right, move 9 more:

                # tod.setheading(90)
                # tod.forward(50)
                # tod.dot(20, random_extracted_color)
                # tod.backward(500)
                # tod.setheading(90)
                # draw_rows_to_right()

                # tod.setheading(90)
                # tod.forward(50)
                # tod.dot(20)
                # tod.setheading(90)
                # tod.forward(50)
                # for _ in range(4):
                #     tod.forward(50)
                #     random_extracted_color = random.choice(color_list)
                #     tod.dot(20, random_extracted_color)

                # tod.setheading(90)


            # if going_right_row == 4:
            #     tod.up()
            #     tod.forward(50 * column)
            #     tod.dot(20, random_extracted_color)
            #
            #     tod.backward(50 * column)
            #     tod.dot(20, random_extracted_color)
            #     for going_left_row in range(1, 9):
            #         random_extracted_color = random.choice(color_list)
            #         tod.dot(20, random_extracted_color)
            #         tod.forward(50)


draw_rows_to_right()


screen = Screen()
screen.exitonclick()