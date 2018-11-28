#!/usr/bin/python

import sys, os

fin = sys.stdin

T = int(fin.readline())

def parse():
    s = ''
    for i in xrange(5):
        s += (fin.readline()[:-1])
    return s

def good(l):
    if '.' in l:
        return False
    if 'X' in l:
        for c in l:
            if c is 'O':
                return None
        return 'x'
    else:
        for c in l:
            if c is 'X':
                return None
        return 'o'

def solve(b):
    # check horizontal
    for i in xrange(4):
        r = good(b[i * 4: i * 4 + 4])
        if r:
            return r
    # check vertical
    for i in xrange(4):
        r = good(b[i::4])
        if r:
            return r
    # check diagonal
    r = good(b[::5])
    if r:
        return r
    r = good(b[3:13:3])
    if r:
        return r
    if '.' in b:
        return -1
    else:
        return 0

for i in xrange(T):
    board = parse()
    #print board
    win = solve(board)
    if win is 'x':
        result = 'X won'
    elif win is 'o':
        result = 'O won'
    elif win is 0:
        result = 'Draw'
    elif win is -1:
        result = 'Game has not completed'
    print 'Case #%d: %s' % (i+1, result)
