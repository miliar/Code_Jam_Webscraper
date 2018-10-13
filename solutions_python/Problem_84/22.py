# -*- coding: utf-8 -*-

import copy
from itertools import groupby

T = int(raw_input())
for case in xrange(1, T + 1):
    R, C = map(int, raw_input().split(' '))
    B = []
    for i in xrange(R):
        B.append([c for c in raw_input()])

    def replace_one(board, xy):
        b = copy.deepcopy(board)
        x, y = xy
        b[y][x:x+2] = ['/', '\\']
        b[y+1][x:x+2] = ['\\', '/']
        return b
    
    def is_not_replacable(board):
        h = len(board)
        w = len(board[0])
        for y in xrange(h):
            for c, l in groupby(board[y]):
                if c != '#':
                    continue
                if len(tuple(l)) & 1 == 1:
                    return True
        board = [[board[y][x] for y in xrange(h)] for x in xrange(w)]
        for y in xrange(w):
            for c, l in groupby(board[y]):
                if c != '#':
                    continue
                if len(tuple(l)) & 1 == 1:
                    return True
        return False

    def find_first(board):
        b = board
        for y in xrange(R - 1):
            for x in xrange(C - 1):
                if '#' == b[y][x] == b[y][x+1] == b[y+1][x] == b[y+1][x+1]:
                    return (x, y)
        return None

    xy = find_first(B)
    while xy and not is_not_replacable(B):
        B = replace_one(B, xy)
        xy = find_first(B)

    print 'Case #%d:' % case

    if is_not_replacable(B):
        print 'Impossible'
    else:
        for y in xrange(R):
            print ''.join(B[y])

