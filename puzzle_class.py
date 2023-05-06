"""
CS5001 Fall 2021
Final Project : Sliding Puzzle Game

Name: Zhuoran Gao
Date: 2021-12-10

Description: This file includes the class designed for the game.
"""
import turtle
import random
import logging
from draw_square import*

# Log error.
logging.basicConfig(filename='5001_puzzle.err', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)

class RName:
    def __init__(self, answer_name, answer_step, puz_image, puz_thumbnail, number):

        # Each tile have different number, create list to store the number of the
        # tiles of the puzzle.
        self.pic_num = []

        # Create list to store the coordinate of the tiles of the puzzle.
        self.pic_pos = []

        # Create list to store the number of the step.
        self.step = []

        # Create variable to store the name of the puzzle according to the puz file.
        self.answer_name = answer_name

        # Create variable to store the step input by player.
        self.answer_step = answer_step

        # Create variable to store the address of the tiles of the puzzle.
        self.puz_image = puz_image

        # Create variable to store the address of the thumbnail of the puzzle.
        self.puz_thumbnail = puz_thumbnail

        # Create variable to store the number of the tiles of the puzzle.
        self.number = number

        # Create variable to store the correct index of the puzzle.
        self.correct = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 'blank']

        # Create variable to store the coordinate of mario.
        self.allpos =[(-345, 170), (-245, 170), (-145, 170), (-45, 170),
                  (-345, 70), (-245, 70), (-145, 70), (-45, 70),
                  (-345, -30), (-245, -30), (-145, -30), (-45, -30),
                  (-345, -130), (-245, -130), (-145, -130), (-45, -130)
                  ]

    def location(self):
        """
        Design the function to change the coordinate for puzzle that
        has different amount of tiles. If the number of tiles is not 16, 9 and 4,
        display the file_error image.
        """
        if self.number == '16':
            self.allpos = [(-345, 170), (-245, 170), (-145, 170), (-45, 170),
                      (-345, 70), (-245, 70), (-145, 70), (-45, 70),
                      (-345, -30), (-245, -30), (-145, -30), (-45, -30),
                      (-345, -130), (-245, -130), (-145, -130), (-45, -130)
                      ]
            self.correct = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 'blank']
        elif self.number == '9':
            self.allpos = [(-345, 170), (-245, 170), (-145, 170),
                      (-345, 70), (-245, 70), (-145, 70),
                      (-345, -30), (-245, -30), (-145, -30),
                      ]
            self.correct = [9, 8, 7, 6, 5, 4, 3, 2, 'blank']
        elif self.number == '4':
            self.allpos = [(-345, 170), (-245, 170),
                      (-345, 70), (-245, 70)
                      ]
            self.correct = [4, 3, 2, 'blank']
        else:
            logger.error('Our puzzles are always squares. Valid numbers are 16 , 9 and 4.')

            # add_picture is a function create in draw_square.py, which can
            # display image in the screen.
            add_picture(0, 0, 'Resources/file_error.gif')
            turtle.delay(500)
            add_picture(0, 0, 'Resources/file_error.gif')
            turtle.bye()

    def add_dic(self, num, pos):
        """
        Design the function to add the number and coordinate of tiles in to list.
        :param num: the number of tiles.
        :param pos: the coordinate of tiles.
        """
        self.pic_num.append(num)
        self.pic_pos.append(pos)

    def empty_dic(self):
        """
        Design a function to help the developer to covert the list
        of number and the list of coordinate to empty list at the same time
        when load other puzzle.
        """
        self.pic_num = []
        self.pic_pos = []

    def get_num(self, pos):
        """
        This function return the number of tiles according
        to the coordinate of the tile.
        :param pos: the coordinate of tiles.
        Return: the number of tiles
        """
        pos_index = self.pic_pos.index(pos)
        return self.pic_num[pos_index]

    def get_pos(self, num):
        """
        This function return the number of tiles according
        to the coordinate of the tile.
        :param pos: the coordinate of tiles.
        Return: the number of tiles
        """
        num_index = self.pic_num.index(num)
        return self.pic_pos[num_index]

    def update_pos(self,pos1,pos2):
        """
        This function helps developer to update the
        coordinate of tiles after player move.
        :param pos1: the tile player move.
        :param pos2: blank tile.
        """
        pos_index1 = self.pic_pos.index(pos1)
        pos_index2 = self.pic_pos.index(pos2)
        num1 = self.pic_num[pos_index1]
        self.pic_num[pos_index1] = self.pic_num[pos_index2]
        self.pic_num[pos_index2] = num1

    def step_account(self):
        """
        This function use list to store step.
        """
        self.step.append(0)
        return len(self.step)

    def step_zero(self):
        """
        This function convert the step to zero when load new puzzle.
        """
        self.step = []
        return len(self.step)

    def add_shape(self, image):
        """
        This function display image on the screen.
        :param image: the address of the tile of puzzle.
        """
        boundary.addshape(image)
        turtle.shape(image)

    def draw_square(self, random_num=False):
        """
        This function draw the tiles of puzzle.
        :param random_num: when reset the puzzle, this parameter is False.
        """

        # Make the list of tiles and coordinate empty.
        self.empty_dic()
        turtle.delay(0)
        turtle.pensize(1)
        turtle.color('black')

        # Create random list to arrange tiles.
        # when reset, change random to refular.
        random_list = []
        for i in range(int(self.number), 1, -1):
            random_list.append(i)
        random_list.append('blank')
        if random_num == True:
            random.shuffle(random_list)

        # Draw the frame of checkerboard and put the tiles in it.
        for i in range(int(self.number)):
            turtle.hideturtle()
            turtle.penup()
            turtle.goto(self.allpos[i])
            turtle.pendown()
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)

            # Find the address of tiles from puz file.
            if random_list[i] == 'blank':
                image = self.puz_image[-1]
            else:
                image = self.puz_image[int(self.number) - random_list[i]]
            self.add_dic(random_list[i], self.allpos[i])
            boundary.addshape(image)
            turtle.penup()
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(50)
            turtle.right(90)
            turtle.shape(image)
            turtle.stamp()
            turtle.pendown()

    def left_right(self, distance_x, blank_x, blank_y):
        """
        This function move the tile to left or right.
        :param distance_x: the distance from blank tile to the tile player moving.
        :param blank_x: x coordinate of blank tile.
        :param blank_y: y coordinate of blank tile.
        """
        turtle.penup()

        # Move the blank tile to the position of tile
        # that player want to move.
        turtle.goto(blank_x + distance_x, blank_y)
        pic_num = self.get_num((blank_x + distance_x, blank_y))
        image = self.puz_image[int(self.number) - pic_num]
        self.add_shape(image)
        turtle.goto(blank_x + 50, blank_y + 50)
        turtle.stamp()

        # Move the tile that player want to move to
        # the position of blank tile.
        self.add_shape(self.puz_image[-1])
        turtle.goto(blank_x + 50 + distance_x, blank_y + 50)
        self.update_pos((blank_x + distance_x, blank_y), (blank_x, blank_y))
        turtle.stamp()

    def up_down(self, distance_y, blank_x, blank_y):
        """
        This function move the tile to up or down.
        :param distance_x: the distance from blank tile to the tile player moving.
        :param blank_x: x coordinate of blank tile.
        :param blank_y: y coordinate of blank tile.
        """
        turtle.penup()

        # Move the blank tile to the position of tile
        # that player want to move.
        turtle.goto(blank_x, blank_y + distance_y)
        pic_num = self.get_num((blank_x, blank_y + distance_y))
        self.add_shape(self.puz_image[int(self.number) - pic_num])
        turtle.goto(blank_x + 50, blank_y + 50)
        turtle.stamp()

        # Move the tile that player want to move to
        # the position of blank tile.
        self.add_shape(self.puz_image[-1])
        turtle.goto(blank_x + 50, blank_y + 50 + distance_y)
        self.update_pos((blank_x, blank_y + distance_y), (blank_x, blank_y))
        turtle.stamp()

    def write_leader(self, leader_board, i):
        t_record.penup()
        t_record.goto(140, 230 - (i) * 30)
        t_record.color('blue')
        t_record.pendown()
        t_record.write(f'{leader_board[i][0]} : {leader_board[i][1]}', font=('Arial', 18))

    def win_lose(self, step_num):
        """
        Judge the win and lose of the game
        :param step_num: the number of move.
        """
        leader_board = []

        # If the move beyond the max move and puzzle is not complete, game lose.
        if step_num > int(self.answer_step) and self.pic_num != self.correct:
            add_picture(0, 0, f'Resources/Lose.gif')
            turtle.delay(500)
            add_picture(0, 0, f'Resources/credits.gif')
            turtle.delay(500)
            add_picture(0, 0, f'Resources/credits.gif')
            turtle.bye()

        # If the move beyond the max move, game lose.
        elif step_num > int(self.answer_step):
            add_picture(0, 0, f'Resources/Lose.gif')
            turtle.delay(500)
            add_picture(0, 0, f'Resources/credits.gif')
            turtle.delay(500)
            add_picture(0, 0, f'Resources/credits.gif')
            turtle.bye()

        # If the step does not beyond and the puzzle is correct, win.
        elif step_num <= int(self.answer_step) and self.pic_num == self.correct:
            record_score.append(step_num)
            record_name.append(self.answer_name)
            try:

                # If win, add the name and score to leader_board.txt
                with open('Leader_board.txt', mode='a+') as write_file:
                    write_file.write(f"{step_num} {self.answer_name}\n")

                # sort the leader_board, select first five to display.
                with open('Leader_board.txt', mode='r') as read_file:
                    num_of_line = 0
                    for line in read_file:
                        num_of_line += 1
                        board_line = list(line.split())
                        leader_board.append(board_line)
                for i in range(len(leader_board)):
                    leader_board[i][0] = int(leader_board[i][0])
                leader_board.sort()
                t_record.clear()
                if num_of_line >= 5:
                    for i in range(5):
                        self.write_leader(leader_board, i)
                else:
                    for i in range(num_of_line):
                        self.write_leader(leader_board, i)
                turtle.color('black')
                add_picture(0, 0, f'Resources/winner.gif')
                turtle.delay(500)
                add_picture(0, 0, f'Resources/winner.gif')
                turtle.bye()
            except FileNotFoundError as err:
                add_picture(0, 0, 'Resources/leaderboard_error.gif')
                logger.error(err)

    def checkerboard(self, x, y, xx, yy):
        """
        Design the scope of x, y coordinate when player move tiles.
        :param x: x coordinate of the tile player want to move.
        :param y: y coordinate of the tile player want to move.
        :param xx: x coordinate of the blank tile.
        :param yy: y coordinate of the blank tile.
        """
        # Limit the scope in the checkboard.
        # This function design the checkboard instead of button.
        if x >= -345 and x <= 55 and y >= -130 and y < 270:

            # Move tile to left.
            if x >= xx-100 and x < xx and y >= yy and y <= yy+100 :
                self.left_right(-100, xx, yy)
                step_num = self.step_account()
                display_step(step_num, self.answer_step)
                self.win_lose(step_num)

            # Move tile to right.
            elif x >= xx + 100 and x < xx + 200 and y >= yy and y <= yy + 100:
                self.left_right(+100, xx, yy)
                step_num = self.step_account()
                display_step(step_num, self.answer_step)
                self.win_lose(step_num)

            # Move tile up.
            elif x >= xx and x <= xx + 100 and y >= yy - 100 and y <= yy:
                self.up_down(-100, xx, yy)
                step_num = self.step_account()
                display_step(step_num, self.answer_step)
                self.win_lose(step_num)

            # Move tile down.
            elif x >= xx and x < xx + 100 and y >= yy + 100 and y <= yy + 200:
                self.up_down(+100, xx, yy)
                step_num = self.step_account()
                display_step(step_num, self.answer_step)
                self.win_lose(step_num)

    def move(self, x, y):
        """
        It is the function in turtle.onclick, which include
        move tiles, reset, load and quit.
        :param x: x coordinate of the click.
        :param y: y coordinate of the click.
        """

        # Find the position of blank tile.
        blank_pos = self.get_pos('blank')
        xx = blank_pos[0]
        yy = blank_pos[1]
        self.checkerboard(x, y, xx, yy)

        # Reset
        if (((x - 70) ** 2+(y + 240) ** 2) ** (0.5)) <= 40:
            turtle.clear()
            self.draw_square()
            self.location()
            for i in range(len(self.correct)):
                self.pic_num[i] = self.correct[i]
            self.checkerboard(x, y, xx, yy)
            add_picture(310, 260, self.puz_thumbnail)

        # Quit
        elif x >= 230 and x < 310 and y >= -265 and y <= -215:
            add_picture(0,0,f'Resources/quitmsg.gif')
            turtle.delay(500)
            add_picture(0, 0, f'Resources/quitmsg.gif')
            boundary.bye()

        # Load.
        elif x >= 130 and x < 210 and y >= -280 and y <= -200:
            load_image = boundary.textinput('Load Puzzle','Enter the name of the puzzle you wish to load. Choces are:\nluigi\nsmiley\nfifteen\nyoshi\nmario')

            # If player input wrong name, quit and log error.
            if load_image != 'luigi' and load_image != 'smiley' and load_image != 'fifteen' and load_image != 'yoshi' and load_image != 'mario':
                add_picture(0, 0, f'Resources/file_error.gif')
                turtle.delay(500)
                add_picture(0, 0, f'Resources/file_error.gif')
                turtle.undo()
                turtle.bye()
                logger.error('Do not have this puzzle')
            else:

                # If player input correct name, load a new puzzle.
                puz_file = load_puz(load_image)
                puz_name = puz_file[0]
                puz_number = puz_file[1]
                puz_size = puz_file[2]
                puz_thumbnail = puz_file[3]
                puz_image = puz_file[4]
                self.puz_image = puz_image
                self.puz_thumbnail = puz_thumbnail
                self.number = puz_number
                self.location()
                turtle.clear()
                self.draw_square(True)
                add_picture(305, 260, self.puz_thumbnail)
                add_leader()
                # Step is zero after load another image.
                self.step_zero()
                display_step(0, self.answer_step)