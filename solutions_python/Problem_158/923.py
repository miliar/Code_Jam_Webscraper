#! /usr/bin/python2

import math


import sys

def parse_input(filename):
        """
        Parse the input according to the following format

        #Test cases

        The input may of course have several test cases
        """
        input_file = open(filename, "r")

        tc_number = int(input_file.readline())
        tc_list = []

        for i in range(tc_number):
                tc = {}
                tc['x'] = i + 1
                tc['X'], tc['R'], tc['C'] = [int(x) for x in input_file.readline().split(' ')]

                tc_list.append(tc)

        return tc_list

def illumino(x, r, c):
    if (x > max(r, c) or math.floor((x + 1)/2) > min(r,c) or (r*c) % x
                      or x >= 7 or (x == 4 and (r <= 2 or c <= 2))):
        return "RICHARD"
    else:
        return "GABRIEL"


def main(argv):
        """
        Our cute main function that will provide some interesting test cases to our
        sexy wizard
        """
        filename = argv[0]
        tc_list = parse_input(filename)

        for tc in tc_list:
            print "Case #%i: %s" % (tc['x'], illumino(tc['X'], tc['R'], tc['C']))

if __name__ == "__main__":
        main(sys.argv[1:])


