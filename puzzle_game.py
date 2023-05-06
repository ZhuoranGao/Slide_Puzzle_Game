"""
CS5001 Fall 2021
Final Project : Sliding Puzzle Game

Name: Zhuoran Gao
Date: 2021-12-10

Description: This file includes the main() function that let the game
running.
"""
import turtle
import random
import logging
from draw_square import*
from puzzle_class import*

def main():
    turtle.screensize(800,650, "white")
    boundary.title('CS5001 Sliding Puzzle Game')
    turtle.speed(1000)
    allpos = [(-345, 170), (-245, 170), (-145, 170), (-45, 170),
              (-345, 70), (-245, 70), (-145, 70), (-45, 70),
              (-345, -30), (-245, -30), (-145, -30), (-45, -30),
              (-345, -130), (-245, -130), (-145, -130), (-45, -130)
              ]

    # Load the mario.
    splash_screen()
    a = pop_up_window()

    # Store the name and step of player.
    answer_name, answer_step = a[0], a[1]
    draw_frame()

    # Open mario puz file, store the information of puz file.
    puz_file = load_puz('mario')
    puz_name = puz_file[0]
    puz_number = puz_file[1]
    puz_size = puz_file[2]
    puz_thumbnail = puz_file[3]
    puz_image = puz_file[4]

    # Draw the checkerboard.
    inst = RName(a[0], a[1], puz_image, puz_thumbnail, puz_number)
    inst.draw_square(True)

    # Add the thumbnail of mario.
    add_picture(310, 260, inst.puz_thumbnail)

    # Add leader board.
    add_leader()

    # Dis play step of mario.
    display_step(0, answer_step)
    boundary.onclick(inst.move)
    boundary.mainloop()
if __name__=='__main__':
    main()

