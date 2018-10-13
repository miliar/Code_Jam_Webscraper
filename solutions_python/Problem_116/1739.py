#!/usr/bin/env python
import sys

i = 0
t = 0
c = 0
board = []

def is_won(row):
    if row.count('.') > 0:
        return 0
    if row.count('X') == 4 or (row.count('X') == 3 and row.count('T') == 1):
        return 1
    elif row.count('O') == 4 or (row.count('O') == 3 and row.count('T') == 1):
        return -1
    return 0

def process(line):
    global t
    global i
    global c
    global board

    i += 1;

    if i == 1:
        t = int(line)
        c = 1
    else:
        board.append(line)

    if len(board) == 4:
        won = 0
        # find win
        for row in board:
            won = is_won(list(row))
            if won != 0:
                break
        if won == 0:
            for x in range(4):
                won = is_won([board[j][x] for j in range(4)])
                if won != 0:
                    break
        if won == 0:
            won = is_won([board[x][x] for x in range(4)])

        if won == 0:
            won = is_won([board[x][3-x] for x in range(4)])

        result = ''
        if won == 1:
            result = 'X won'
        elif won == -1:
            result = 'O won'
        else:
            if ''.join(board).count('.') == 0:
                result = 'Draw'
            else:
                result = 'Game has not completed'

        print "Case #{}: {}".format(c, result)
        c += 1
        board = []


if len(sys.argv) < 2:
    print "Please supply the input file as argument"
    sys.exit(2)

filename = sys.argv[1]
with open(filename) as f:
    for line in f:
        if len(line.strip()):
            process(line.strip())

