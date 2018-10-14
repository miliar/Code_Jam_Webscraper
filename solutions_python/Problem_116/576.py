#!/usr/bin/env python
from sys import stdin, stdout
from itertools import *

def winning_line(l, player):
    l = l.replace('T', player)
    return l == player*4

def won(data, player):
    cases = list(data)

    for cn in range(4):
        c = ''.join(data[rn][cn] for rn in range(4))
        cases.append(c)

    cases.append(''.join(data[x][x] for x in range(4)))
    cases.append(''.join(data[3-x][x] for x in range(4)))

    for case in cases:
        if winning_line(case, player):
            return True
    return False

def answer(data):
    if won(data, 'X'):
        return 'X won'
    if won(data, 'O'):
        return 'O won'
    for l in data:
        if '.' in l:
            return 'Game has not completed'
    return 'Draw'

def cases(s):
    while 1:
        d = [next(s).rstrip() for x in range(4)]
        next(s)
        yield d

if __name__ == '__main__':
    stdin.next()
    for n,case in enumerate(cases(stdin)):
        print "Case #%d: %s" % (n+1, answer(case))
