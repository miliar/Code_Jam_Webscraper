# -*- coding: utf-8 -*-

"""
Script to solve the problem Tic-Tac-Toe-Tomek from Google Code Jam 2013.

Author: Jonatas Oliveira
Email: jonatas.oliveira@gmail.com
Site: http://www.nerdwho.com/
"""

import sys
import os

def read_file(filepath):
    """Opens the filepath and return a tuple of number of test cases and
    the list of the lines in the file.
    """
    f = open(file_path)
    n = int(f.readline().strip('\n\t'))
    result = [x.strip('\n\t') for x in f.readlines()]
    return n, result

def print_output(status, case_number):
    if status in ('X', 'O'):
        msg = '%s won' % status
    elif status == 'draw':
        msg = 'Draw'
    else:
        msg = 'Game has not completed'
    print 'Case #%s: %s' % (case_number, msg)

def determine_line_won(line, case_number):
    """Determines the line status."""
    if '.' in line:
        return False

    line = line.replace('T', '')
    if line == 'XXX' or line == 'XXXX':
        print_output('X', case_number)
        return True
    elif line == 'OOO' or line == 'OOOO':
        print_output('O', case_number)
        return True

def determine_draw_or_not_completed(lines, case_number):
    """Determines the if the board has a draw or the game was not completed."""
    flat_lines = ''.join(lines)
    if '.' in flat_lines:
        print_output('not_completed', case_number)
    else:
        print_output('draw', case_number)

def determine_board_status(lines, case_number):
    """Receive all lines of the game and return the board status."""
    for line in lines:
        if determine_line_won(line, case_number):
            return

    lines_transposed = [''.join(l) for l in zip(*lines)]
    for line in lines_transposed:
        if determine_line_won(line, case_number):
            return

    top_left_down = '%s%s%s%s' % (lines[0][0], lines[1][1], lines[2][2], lines[3][3])
    if determine_line_won(top_left_down, case_number):
        return

    top_right_down = '%s%s%s%s' % (lines[0][3], lines[1][2], lines[2][1], lines[3][0])
    if determine_line_won(top_right_down, case_number):
        return

    return determine_draw_or_not_completed(lines, case_number)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = os.path.join(os.path.dirname(__file__), 'sample_input.txt')

    n, result = read_file(file_path)
    for i in range(n):
        lines = result[i*5:i*5+4]
        determine_board_status(lines, i + 1)

