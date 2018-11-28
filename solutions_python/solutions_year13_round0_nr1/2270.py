# coding: utf-8
from IPython.nbformat import current
from numpy.distutils.system_info import _numpy_info

__author__ = 'edubecks'

#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Created on April 12, 2013
@author: edubecks
"""

import os
import sys
import fileinput


NOT_COMPLETED = 0
X = 1
O = 11
DRAW = -100
DEBUG = False

def check_draw(board):
## check if ended game
    for row in board:
        if 0 in row:
            return False

    return True

def check_winner(board, player):
    win = player * 4

    ##horizontal
    for row in board:
        if sum(row) == win:
            if DEBUG: print 'horizontal', row
            return True

    ## transpose
    board_t = zip(*board)
    # print board
    # print board_t
    for row in board_t:
        if sum(row) == win:
            if DEBUG: print 'vertical', board_t
            return True

    ## diagonal
    diagonal_1 = [board[c][c] for c in xrange(4)]
    if sum(diagonal_1) == win:
        if DEBUG: print 'diag1', diagonal_1
        return True

    diagonal_2 = [board[3 - c][c] for c in xrange(4)]
    if sum(diagonal_2) == win:
        if DEBUG: print 'diag2', diagonal_2
        return True

    return False


def main():
    input_test = [line.strip() for line in fileinput.input()]

    num_tests = int(input_test[0])

    current_line = 1

    values_X = {
        '.': 0,
        'X': X,
        'O': O,
        'T': X
    }

    values_O = {
        '.': 0,
        'X': X,
        'O': O,
        'T': O
    }

    winners_case = {
        (True, True): 'Game has not completed',
        (True, False): 'X won',
        (False, True): 'X won',
        (False, False): 'Draw',
    }

    current_line-=5;

    for test in xrange(num_tests):
        current_line += 5

        winner = [False, False]

        ## X
        board = []
        for i in xrange(4):
            alt = input_test[current_line + i]
            alt = [values_X[c] for c in alt]
            board.append(alt)
        if check_winner(board, X):
            print 'Case #' + str(test+1) + ': X won'
            continue

        ## O
        board = []
        for i in xrange(4):
            alt = input_test[current_line + i]
            alt = [values_O[c] for c in alt]
            board.append(alt)
        if check_winner(board, O):
            print 'Case #' + str(test + 1) + ': O won'
            continue

        if check_draw(board):
            print 'Case #' + str(test + 1) + ': Draw'
        else:
            print 'Case #' + str(test + 1) + ': Game has not completed'


    return


if __name__ == '__main__':
    main()
