#!/usr/bin/env python

from __future__ import print_function
import sys

def pressbuttons(buttons, o_buttons, b_buttons):
    turns = 0

    o_bot = 1
    b_bot = 1
    for button in buttons:
        while(True):
            button_pressed = False

            if(len(o_buttons) <= 0 and len(b_buttons) <= 0):
                break
            # elif(len(o_buttons) <= 0):
                # print("button:", button, "|| orange bot:", o_bot, "->  | blue bot:", b_bot, "->", b_buttons[0])
            # elif(len(b_buttons) <= 0):
                # print("button:", button, "|| orange bot:", o_bot, "->", o_buttons[0], "| blue bot:", b_bot, "-> ")
            # else:
                # print("button:", button, "|| orange bot:", o_bot, "->", o_buttons[0], "| blue bot:", b_bot, "->", b_buttons[0])

            turns=turns+1

            if(button[0] == "O" and o_bot == int(button[1:])):
                o_buttons.pop(0)
                button_pressed = True
            elif(len(o_buttons) > 0):
                if(o_bot < o_buttons[0]):
                    o_bot = o_bot + 1
                elif(o_bot > o_buttons[0]):
                    o_bot = o_bot - 1

            if(button[0] == "B" and b_bot == int(button[1:])):
                b_buttons.pop(0)
                button_pressed = True
            elif(len(b_buttons) > 0):
                if(b_bot < b_buttons[0]):
                    b_bot = b_bot + 1
                elif(b_bot > b_buttons[0]):
                    b_bot = b_bot - 1

            if(button_pressed):
                break

    return turns

def main(*args):
    if(len(args) < 2):
        print("Usage: %s <input file>" % args[0])

    filename = args[1]
    input_file = open(filename, "rb")
    output_file = open(filename+".out", "wb")

    try:
        input = input_file.readline().strip()
    except:
        print("Premature end of input")

    T = int(input)
    for j in range(T):
        try:
            inputs = input_file.readline().split()
        except:
            print("Premature end of input")

        N = int(inputs[0])
        button_list = []
        o_buttons = []
        b_buttons = []
        for i in range(N):
            button_list.append(inputs[2*i+1]+inputs[2*i+2])
            if(inputs[2*i+1] == "O"):
                o_buttons.append(int(inputs[2*i+2]))
            elif(inputs[2*i+1] == "B"):
                b_buttons.append(int(inputs[2*i+2]))

        # print(button_list, o_buttons, b_buttons)
        turns = pressbuttons(button_list, o_buttons, b_buttons)
        # print("Case #%d: %d" % (j+1, turns))
        print("Case #%d: %d" % (j+1, turns), file=output_file)

    input_file.close()
    output_file.close()


if(__name__ == "__main__"):
    sys.exit(main(*sys.argv))
