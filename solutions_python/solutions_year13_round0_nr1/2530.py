#!/usr/bin/env python

import sys

num = int(sys.stdin.readline())

boards = sys.stdin.read().strip()
boards = boards.split('\n\n')
boards = [brd.split('\n') for brd in boards]


def transpose(brd):
    newbrd = []
    for it in range(4):
        newbrd.append(''.join([line[it] for line in brd]))
    return newbrd


def check_line(line, mark):
    if line.count(mark) == 4 or (line.count(mark) == 3 and 'T' in line):
        return True
    else:
        return False


def check_diag(brd, mark):
    diag0 = [brd[it][it] for it in range(4)]
    diag1 = [brd[it][3-it] for it in range(4)]
    return check_line(diag0, mark) or check_line(diag1, mark)


def determine(brd):
    tbrd = transpose(brd)
    for it in range(4):
        line = brd[it]
        column = tbrd[it]
        if check_line(line, 'X') or check_line(column, 'X') or \
           check_diag(brd, 'X'):
            return 'X won'
        if check_line(line, 'O') or check_line(column, 'O') or \
           check_diag(brd, 'O'):
            return 'O won'
    if ''.join(brd).count('.') != 0:
        return 'Game has not completed'
    else:
        return 'Draw'


for it, brd in enumerate(boards):
    print('Case #%d: %s' % (it+1, determine(brd)))
