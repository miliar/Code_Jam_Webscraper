#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def get_status(board):
    for row in board:
        if all([cell == 'O' or cell == 'T' for cell in row]):
            return 'O won'
        if all([cell == 'X' or cell == 'T' for cell in row]):
            return 'X won'
    for i in xrange(4):
        col = [row[i] for row in board]
        if all([cell == 'O' or cell == 'T' for cell in col]):
            return 'O won'
        if all([cell == 'X' or cell == 'T' for cell in col]):
            return 'X won'

    diagonal = [board[i][i] for i in xrange(4)]
    if all([cell == 'O' or cell == 'T' for cell in diagonal]):
        return 'O won'
    if all([cell == 'X' or cell == 'T' for cell in diagonal]):
        return 'X won'
    diagonal = [board[3-i][i] for i in xrange(4)]
    if all([cell == 'O' or cell == 'T' for cell in diagonal]):
        return 'O won'
    if all([cell == 'X' or cell == 'T' for cell in diagonal]):
        return 'X won'

    for row in board:
        if '.' in row:
            return 'Game has not completed'

    return 'Draw'



def main():
    T = int(sys.stdin.readline())

    for i in range(1, T+1):
        board = [list(sys.stdin.readline().strip()) for _ in xrange(4)]
        sys.stdin.readline()
        print "Case #%d: %s" % (i, get_status(board))

if __name__ == '__main__':
    main()

