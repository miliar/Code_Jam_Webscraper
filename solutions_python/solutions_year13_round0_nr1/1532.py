#!/usr/bin/python

import sys

def line(a, b, c, d):
    return (a == b or b == 'T') and (a == c or c == 'T') and (a == d or d == 'T')

def check(i, j, b):
    if i == 0 and j == 0:
        if line(b[i][j], b[i+1][j+1], b[i+2][j+2], b[i+3][j+3]):
            return b[i][j]
    elif i == 0 and j == 3:
        if line(b[0][3], b[1][2], b[2][1], b[3][0]):
            return b[0][3]
    if i == 0:
        if line(b[0][j], b[1][j], b[2][j], b[3][j]):
            return b[0][j]
    if j == 0:
        if line(b[i][0], b[i][1], b[i][2], b[i][3]):
            return b[i][0]
    return ''

cases = int(sys.stdin.readline())
for case in range(1,cases+1):
    board = [[],[],[],[]]
    board[0] = list(sys.stdin.readline().rstrip())
    board[1] = list(sys.stdin.readline().rstrip())
    board[2] = list(sys.stdin.readline().rstrip())
    board[3] = list(sys.stdin.readline().rstrip())
    ended = True
    won = ''
    i = 0
    while i < 4 and won == '':
        if board[0][i] != '.':
            won = check(0, i, board)
        else:
            ended = False
        i = i + 1
    i = 0
    while i < 4 and won == '':
        if board[i][0] != '.':
            won = check(i, 0, board)
        else:
            ended = False
        i = i + 1
    W = "Game has not completed"
    if won:
        W = won + " won"
    elif ended:
        i = 1
        while ended and i < 4:
            j = 1
            while ended and j < 4:
                if board[i][j] == '.':
                    ended = False
                j = j + 1
            i = i + 1
        if ended:
            W = "Draw"
    print "Case #"+str(case)+": "+str(W)
    sys.stdin.readline()
