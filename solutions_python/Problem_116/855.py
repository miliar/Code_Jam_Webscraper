#!/usr/bin/env python

import math
import sys

# Global variables
output_file = None
current_case = 1
DEBUG = True
N = 4


# The main method which will receive a parsed input file
def jam(lines):
    # Fixed number of lines
    for i in range(1, len(lines), 5):
        print_solution(get_state(lines[i:i+4]))


# Case-specific program
def get_state(field):
    open_fields = N * N

    # Check lines
    for row in range(N):
        player = None
        seq = 0
        for col in range(N):
            if field[row][col] == '.':
                player = '.'
                seq = 0
            elif field[row][col] == 'T':
                open_fields -= 1
                player = player if player is not None else 'T'
                seq += 1
            elif field[row][col] in ['X', 'O']:
                open_fields -= 1
                if player is None or player == 'T' or player == field[row][col]:
                    player = field[row][col]
                    seq += 1
                else:
                    seq = 0
                    player = '.'
        if seq == N:
            return ('%s won' % player)

    # Check rows
    for col in range(N):
        player = None
        seq = 0
        for row in range(N):
            if field[row][col] == '.':
                player = '.'
                seq = 0
            elif field[row][col] == 'T':
                player = player if player is not None else 'T'
                seq += 1
            elif field[row][col] in ['X', 'O']:
                if player is None or player == 'T' or player == field[row][col]:
                    player = field[row][col]
                    seq += 1
                else:
                    seq = 0
                    player = '.'
        if seq == N:
            return ('%s won' % player)

    # Check diagonals
    # BL -> TR
    player = None
    seq = 0
    for i in range(N):
        if field[i][i] == '.':
            player = '.'
            seq = 0
        elif field[i][i] == 'T':
            player = player if player is not None else 'T'
            seq += 1
        elif field[i][i] in ['X', 'O']:
            if player is None or player == 'T' or player == field[i][i]:
                player = field[i][i]
                seq += 1
            else:
                seq = 0
                player = '.'

    if seq == N:
        return ('%s won' % player)

    # TL -> BR
    player = None
    seq = 0
    for i in range(N):
        if field[N-1-i][i] == '.':
            player = '.'
            seq = 0
        elif field[N-1-i][i] == 'T':
            player = player if player is not None else 'T'
            seq += 1
        elif field[N-1-i][i] in ['X', 'O']:
            if player is None or player == 'T' or player == field[N-1-i][i]:
                player = field[N-1-i][i]
                seq += 1
            else:
                seq = 0
                player = '.'

    if seq == N:
        return ('%s won' % player)

    if open_fields > 0:
        return "Game has not completed"
    else:
        return "Draw"


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
