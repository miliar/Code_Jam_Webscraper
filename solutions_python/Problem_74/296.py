#!/usr/bin/python

import sys

# Read in input
num_problems = int(sys.stdin.readline())

for problem_number in range(1, num_problems + 1):
    # Read problem input
    tokens = sys.stdin.readline().split(' ')
    num_buttons = int(tokens[0])
    orange_position = blue_position = 1
    orange_command = blue_command = 0
    next_button = 0
    commands = []
    for robot, button in zip(tokens[1:len(tokens):2], tokens[2:len(tokens):2]):
        commands.append((robot, int(button)))

    seconds = command_index = 0
    while True:
        orange_moved = blue_moved = 0
        # Test for completion
        if next_button >= num_buttons:
            break
        # scan to the next orange command
        while orange_command < num_buttons and commands[orange_command][0] != 'O': 
            orange_command += 1
        # scan to the next blue command
        while blue_command < num_buttons and commands[blue_command][0] != 'B':
            blue_command += 1
        # move orange if he is not in position
        if orange_command < num_buttons and commands[orange_command][1] < orange_position:
            orange_position -= 1
            orange_moved = 1
        elif orange_command < num_buttons and commands[orange_command][1] > orange_position:
            orange_position += 1
            orange_moved = 1
        # move blue if he is not in position
        if blue_command < num_buttons and commands[blue_command][1] < blue_position:
            blue_position -= 1
            blue_moved = 1
        elif blue_command < num_buttons and commands[blue_command][1] > blue_position:
            blue_position += 1
            blue_moved = 1
        # If orange has not moved, and he is in position,
        # and it is his turn, push the button and go to next command in queue
        if not orange_moved and orange_command < num_buttons and commands[orange_command][1] == orange_position and orange_command == next_button:
            next_button += 1
            orange_command += 1
        # If orange didn't press a button, and blue has not moved,
        # and he is in position, and it is his turn, push the button and go to next command in queue
        elif not blue_moved and blue_command < num_buttons and commands[blue_command][1] == blue_position and blue_command == next_button:
            next_button += 1
            blue_command += 1
        seconds += 1

    # Output answer
    print "Case #" + str(problem_number) + ":", seconds
