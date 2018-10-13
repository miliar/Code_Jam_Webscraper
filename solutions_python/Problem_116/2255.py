#!/usr/bin/env python

import os, sys


def solve (board):
    gameComplete = True

    d1 = board[0][0] + board[1][1] + board[2][2] + board[3][3] 
    d2 = board[0][3] + board[1][2] + board[2][1] + board[3][0] 

    if d1.replace('T','X') == "XXXX":
        return 'X won'
    if d1.replace('T','O') == "OOOO":
        return 'O won'
    if d2.replace('T','X') == "XXXX":
        return 'X won'
    if d2.replace('T','O') == "OOOO":
        return 'O won'

    for row in board:
        if row.replace('T','X') == "XXXX":
            return 'X won'
        if row.replace('T','O') == "OOOO":
            return 'O won'
        if gameComplete and '.' in row:
            gameComplete = False

    board = [''.join(x) for x in zip(*board[::-1])]
    for row in board:
        if row.replace('T','X') == "XXXX":
            return 'X won'
        if row.replace('T','O') == "OOOO":
            return 'O won'

    if gameComplete:
        return "Draw"
    return "Game has not completed"


fd = sys.stdin

line = fd.readline()
sets = int(line)+1

for case in xrange(1, sets):
    board = []
    for row in xrange(4):
        line = fd.readline().strip()
        board.append(line.strip())
    nline = solve(board)
    fd.readline()
    print "Case #%s: %s" % (case, nline)

fd.close()
