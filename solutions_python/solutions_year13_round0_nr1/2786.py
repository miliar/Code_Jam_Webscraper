#!/usr/bin/env python
import sys

def is_o(x):
    if  x=='O' or x=='T':
        return 1
    else:
        return 0

def is_x(x):
    if  x=='X' or x=='T':
        return 1
    else:
        return 0

def o_win(row):
    if sum(map(is_o, row)) == 4:
        return 1
    else:
        return 0

def x_win(row):
    if sum(map(is_x, row)) == 4:
        return 1
    else:
        return 0

def not_full(row):
    if len(filter(lambda x: x == '.', row)) > 0:
        return 1
    else:
        return 0

def check_horizontal(board):
    not_draw = 0
    for i in range(4):
        row = board[i]
        if o_win(row) == 1:
            return 'O won'
        elif x_win(row) == 1:
            return 'X won'
        elif not_full(row) == 1:
            not_draw = 1
    if not_draw == 1:
        return 'Game has not completed'
    else:
        return 'Draw'


def check_vertical(board):
    not_draw = 0
    for i in range(4):
        row = map(lambda x: x[i], board)
        if o_win(row) == 1:
            return 'O won'
        elif x_win(row) == 1:
            return 'X won'
        elif not_full(row) == 1:
            not_draw = 1
    if not_draw == 1:
        return 'Game has not completed'
    else:
        return 'Draw'

def check_cross(board):
    lr = []
    rl = []
    for i in range(4):
        lr.append(board[i][i])
        rl.append(board[i][3-i])
    if o_win(lr) == 1 or o_win(rl) == 1:
        return 'O won'
    elif x_win(lr) == 1 or x_win(rl) == 1:
        return 'X won'
    return 'Draw'


n = int(sys.stdin.readline().strip())

for i in range(1, n+1):
    board=[]
    for j in range(4):
        line = sys.stdin.readline().strip().strip()
        row = []
        for char in line:
            row.append(char)
        board.append(row)
    resh = check_horizontal(board)
    resv = check_vertical(board)
    resc = check_cross(board)
    if resh == 'Draw' and resv == 'Draw':
        print 'Case #%d: %s' % (i, resh)
    elif resh == 'O won' or resv == 'O won' or resc == 'O won':
        print 'Case #%d: O won' % (i)
    elif resh == 'X won' or resv == 'X won' or resc == 'X won':
        print 'Case #%d: X won' % (i)
    elif resh == 'Game has not completed' and resv == 'Game has not completed':
        print 'Case #%d: %s' % (i, resh)
    else:
        print 'ERROR!!!'
    sys.stdin.readline()



