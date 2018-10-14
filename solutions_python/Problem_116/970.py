#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import sys
import numpy as np


def solve(board):
    lines = board
    columns = [list(line) for line in np.array(board).T]
    spaces = 0
    
    for i in xrange(4):
        line = lines[i]
        column = columns[i]
        spaces += line.count(0)
        if line.count(1) == 4 or (line.count(1) == 3 and line.count(3) == 1) or column.count(1) == 4 or (column.count(1) == 3 and column.count(3) == 1):
            return 'X won'
        if line.count(2) == 4 or (line.count(2) == 3 and line.count(3) == 1) or column.count(2) == 4 or (column.count(2) == 3 and column.count(3) == 1):
            return 'O won'

    diagonals = [
        [board[i][i] for i in xrange(4)],
        [board[i][-(i + 1)] for i in xrange(4)]
    ]
    
    if diagonals[0].count(1) == 4 or (diagonals[0].count(1) == 3 and diagonals[0].count(3) == 1) or diagonals[1].count(1) == 4 or (diagonals[1].count(1) == 3 and diagonals[1].count(3) == 1):
        return 'X won'
    if diagonals[0].count(2) == 4 or (diagonals[0].count(2) == 3 and diagonals[0].count(3) == 1) or diagonals[1].count(2) == 4 or (diagonals[1].count(2) == 3 and diagonals[1].count(3) == 1):
        return 'O won'

    if spaces == 0:
        return 'Draw'

    return 'Game has not completed'


def main():
    for case in xrange(int(sys.stdin.readline().strip())):
        board = []
        for i in xrange(4):
            board.append(
                [
                    {
                        '.': 0,
                        'X': 1,
                        'O': 2,
                        'T': 3
                    }[piece] for piece in sys.stdin.readline().strip()
                ]
            )
        print 'Case #%d: %s' % (
            case + 1,
            solve(board)
        )
        trash = sys.stdin.readline()

    return 0

if __name__ == '__main__':
    sys.exit(main())
