#!/usr/bin/python2
# -*- coding: utf8 -*-
# Google Code Jam 2013 - Qualification Round - Problem A - Mateusz Kurek
# import io
# import numpy as np

# raw_input = input
# xrange = range

BOARD_SIZE = 4
JOCKER = 10
DIAGONALS = (
    ((0, 0), (1, 1), (2, 2), (3, 3)),
    ((0, 3), (1, 2), (2, 1), (3, 0))
)


def check_sum(s):
    r = {
        BOARD_SIZE: 1,
        -BOARD_SIZE: -1,
        BOARD_SIZE + JOCKER - 1: 1,
        -BOARD_SIZE + JOCKER + 1: -1
    }
    return r.get(s, 0)


def solve_case():
    subst = {
        'X': 1,
        'O': -1,
        '.': 0,
        'T': JOCKER
    }
    board = []
    empty = 0
    for i in range(BOARD_SIZE):
        row = map(lambda x: subst.get(x, 0), raw_input().strip())
        empty += row.count(0)
        board.append(row)

    for row in board:
        row_sum = sum(row)
        row_result = check_sum(row_sum)
        if row_result != 0:
            return row_result

    # columns
    for i in range(BOARD_SIZE):
        column_sum = 0
        for j in range(BOARD_SIZE):
            column_sum += board[j][i]
        column_result = check_sum(column_sum)
        if column_result != 0:
            return column_result

    # diagonals
    for d in DIAGONALS:
        diag_sum = 0
        for row, col in d:
            diag_sum += board[row][col]
        diag_result = check_sum(diag_sum)
        if diag_result != 0:
            return diag_result

    if not empty:
        return 0

    return 2


def main():
    winner = {
        -1: 'O won',
        0: 'Draw',
        1: 'X won',
        2: 'Game has not completed'
    }

    t = int(raw_input())
    result = []
    for tc in xrange(1, t+1):
        win = solve_case()
        result.append("Case #{tc}: {win}".format(tc=tc, win=winner.get(win)))
        # empty line
        try:
            raw_input()
        except EOFError:
            pass

    print "\n".join(result)

if __name__ == '__main__':
    main()
