#!/usr/bin/python

import sys


def readint(f):
    return int(f.readline())

def readmatrix(f, rows):
    matrix = []
    for i in xrange(rows):
        matrix += [f.readline().strip()]
    return matrix

def check(v, x):
    return all([c == x or c == 'T' for c in v])

def who(board):
    for r in xrange(4):
        row = [board[r][i] for i in xrange(4)]
        if check(row, 'X'):
            return 'X won'
        elif check(row, 'O'):
            return 'O won'
    for c in xrange(4):
        row = [board[i][c] for i in xrange(4)]
        if check(row, 'X'):
            return 'X won'
        elif check(row, 'O'):
            return 'O won'
    diag1 = [board[0][0], board[1][1], board[2][2], board[3][3]]
    diag2 = [board[0][3], board[1][2], board[2][1], board[3][0]]
    if check(diag1, 'X') or check(diag2, 'X'):
        return 'X won'
    elif check(diag1, 'O') or check(diag2, 'O'):
        return 'O won'
    elif any(board[i][j] == '.' for i in xrange(4) for j in xrange(4)):
        return 'Game has not completed'
    else:
        return 'Draw'

if __name__ == "__main__":
    f = open(sys.argv[1], "r")
    numCases = readint(f)
    for i in xrange(numCases):
        print "Case #%d:" % (i + 1),
        board = readmatrix(f, 4)
        f.readline()
        print who(board)
