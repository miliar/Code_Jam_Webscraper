#!/usr/bin/env python

import math
import sys

# Global variables
output_file = None
current_case = 1
DEBUG = True


# The main method which will receive a parsed input file
def jam(lines):
    # Variable number of lines
    line = 1
    while line < len(lines):
        rows, cols = map(int, lines[line].split())
        line += 1
        print_solution(is_mowable(lines[line:line+rows], rows, cols))
        line += rows


# Case-specific program
def is_mowable(field, rows, cols):
    # Parse field
    for i in range(rows):
        field[i] = map(int, field[i].split())

    # From the left and upper edge, mow with the maximum height inside that
    # desired field in order not to cut too much away, then check if the fields
    # match
    own = [[100 for i in range(cols)] for j in range(rows)]

    for row in range(rows):
        height = get_max_in_row(field, row)
        own = mow_row(own, row, height)

    for col in range(cols):
        height = get_max_in_col(field, col)
        own = mow_col(own, col, height)

    if field == own:
        return "YES"
    else:
        return "NO"

def get_max_in_row(field, row):
    return max(field[row])

def get_max_in_col(field, col):
    cur_max = 0
    for i in range(len(field)):
        if field[i][col] > cur_max:
            cur_max = field[i][col]

    return cur_max

def mow_row(field, row, height):
    for col in range(len(field[row])):
        field[row][col] = min(field[row][col], height)
    return field

def mow_col(field, col, height):
    for row in range(len(field)):
        field[row][col] = min(field[row][col], height)
    return field


# Boilerplate: method for printing a result
def print_solution(solution):
    global current_case
    global output_file
    result = "Case #%d: %s" % (current_case, solution)
    current_case += 1
    output_file.write(result + "\n")
    if DEBUG:
        print result


# Main entry point, parses input and prepares output file
if __name__ == "__main__":
    lines = []
    filename = "%s-%s-%s" % (sys.argv[1], sys.argv[2], sys.argv[3])
    input_file = file(filename + ".in")
    output_file = file(filename + ".out", 'w')

    for line in input_file:
        lines.append(line.rstrip('\n'))

    jam(lines)
