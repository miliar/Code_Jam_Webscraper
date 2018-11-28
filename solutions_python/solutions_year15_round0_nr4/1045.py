#!/usr/bin/python

import sys

def convert_input(char_list):
    result_list = []

    for char in char_list:
        if char.isdigit():
            result_list.append(int(char))

    return result_list


def game(num_list):
    X = num_list[0]
    R = num_list[1]
    C = num_list[2]

    if R*C < 2*X:
        if R*C <= 2 and (X == R or X == C):
            return "GABRIEL"
        else:
            return "RICHARD"
    elif R*C == 2*X:
        if X == 4:
            return "RICHARD"
        else:
            return "GABRIEL"
    else:
        if (R*C) % X != 0:
            return "RICHARD"
        else:
            return "GABRIEL"

def run():
    if len(sys.argv) < 2:
        print "Need input file name!!\n"
        return

    in_name = str(sys.argv[1])
    fo_in = open(in_name, "r")

    total_cases = int(fo_in.readline())

    for idx in xrange(total_cases):
        char_list = list(fo_in.readline())
        num_list = convert_input(char_list)
        winner = game(num_list)
        print "Case #%d: %s"%(idx+1, winner)


    fo_in.close()

run()
