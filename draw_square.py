"""
CS5001 Fall 2021
Final Project : Sliding Puzzle Game

Name: Zhuoran Gao
Date: 2021-12-10

Description: This file includes all the function for the game.
"""
import turtle
import random
import logging

boundary = turtle.Screen()
step = []

# Create different turtle so that developer can
# clear the screen conveniently.
t1 = turtle.Turtle()
t1.hideturtle()
t_frame = turtle.Turtle()
t_frame.hideturtle()
t_record = turtle.Turtle()
t_picture = turtle.Turtle()
t_leader = turtle.Turtle()

# The correct order of tiles.
correct = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 'blank']
record_name = []
record_score = []

# Log error.
logging.basicConfig(filename='5001_puzzle.err', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)

def splash_screen():
    """
    Design splash screen
    """
    turtle.goto(0, 0)
    image = f'Resources/splash_screen.gif'
    boundary.addshape(image)
    turtle.shape(image)
    turtle.stamp()
    turtle.delay(900)
    turtle.clear()

def pop_up_window():
    """
    Design pop up window.
    """
    turtle.clearscreen()
    try:
        answer_name = boundary.textinput("CS5001 Puzzle Slide", "Your name:")
    except:
        logger.error('Did not have the answer_name')
    try:
        answer_step = int(turtle.numinput("5001 Puzzle Slide - Moves", "Enter the number of moves(chances)you want(5-200)", default=None, minval=5, maxval=200))
    except:
        logger.error('Did not have the answer_step')
    return answer_name, answer_step

def load_puz(answer_name):
    """
    Load puz file.
    :param answer_name: the name player input.
    :return: the information in the file.
    """
    puz_dic = []
    answer_name = answer_name + '.puz'
    try:
        with open(answer_name, mode='r') as file:
            for line in file:
                file = list(line.split())
                puz_dic.append(file[1])
        name = puz_dic[0]
        puz_dic.pop(0)
        number = puz_dic[0]
        puz_dic.pop(0)
        size = puz_dic[0]
        puz_dic.pop(0)
        thumbnail = puz_dic[0]
        puz_dic.pop(0)
    except :
        logger.error('We can not load this file since we do not have this puzzle')
    return name, number, size, thumbnail, puz_dic

def display_step(step, answer_step):
    """
    Design function to display step.
    :param step: the step player have already move.
    :param answer_step: the step player choose.
    """
    t1.clear()
    t1.hideturtle()
    t1.penup()
    t1.goto(-70, -250)
    t1.color('black')
    t1.write(f'Player moves:{step}/{answer_step}', align="right", font=('Arial', 22, "bold"))

def add_picture(x, y, image):
    """
    This function add image to turtle.
    :param x: x coordinate of image.
    :param y: y coordinate of image.
    :param image: the address of the image.
    """
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    boundary.addshape(image)
    turtle.shape(image)
    turtle.stamp()

def add_leader():
    """
    Add the worder of leader.
    """
    t_leader.penup()
    t_leader.goto(135, 260)
    t_leader.pendown()
    t_leader.color('blue')
    t_leader.write('leaders:', font=('Arial', 18))
    t_leader.color('black')

def add_button(x, y, image):
    """
    :param x: x coordinate of the button.
    :param y: y coordinate of the button.
    :param image: address of the button.
    """
    t_frame.goto(x, y)
    boundary.addshape(image)
    t_frame.shape(image)
    t_frame.stamp()

def draw_frame():
    """
    Draw the frame of the game.
    """
    # Big black frame for the puzzle.
    t_frame.hideturtle()
    t_frame.pensize(10)
    t_frame.color('white')
    t_frame.speed(1000)
    t_frame.goto(-370, 295)
    t_frame.pendown()
    t_frame.penup()
    t_frame.goto(-370, 295)
    t_frame.pendown()
    t_frame.color('black')
    t_frame.goto(80, 295)
    t_frame.goto(80, -155)
    t_frame.goto(-370, -155)
    t_frame.goto(-370, 295)

    # Small black frame for button
    t_frame.penup()
    t_frame.goto(-370, -190)
    t_frame.pendown()
    t_frame.goto(330, -190)
    t_frame.goto(330, -290)
    t_frame.goto(-370, -290)
    t_frame.goto(-370, -190)

    # Draw the blue frame.
    t_frame.color('blue')
    t_frame.penup()
    t_frame.goto(120, 295)
    t_frame.pendown()
    t_frame.goto(330, 295)
    t_frame.goto(330, -155)
    t_frame.goto(120, -155)
    t_frame.goto(120, 295)
    t_frame.penup()

    # Place the buttons.
    add_button(70, -240, 'Resources/resetbutton.gif')
    add_button(170, -240, 'Resources/loadbutton.gif')
    add_button(270, -240, 'Resources/quitbutton.gif')
