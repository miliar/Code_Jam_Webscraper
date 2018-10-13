#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from sys import stderr
from collections import deque
from itertools import *
data = deque(sys.stdin.read().split())
token = data.popleft
T = int(token())

def test():
    v = []
    for c in range(4):
        v.append(token())

    def find(dx, dy, xs, ys, tk):
        for x in range(4):
            if v[xs][ys] == tk:
                return True
            xs, ys = xs+dx, ys+dy
        return False

    #print v

    for dx,dy in product((-1,0,1), (0, 1)):
        if dx == dy == 0:
            continue
        for xs,ys in chain(product(range(4), (0,)), product((0,),
                range(4))):
            try:
                if find(dx,dy,xs,ys, '.') or \
                        (find(dx,dy,xs,ys, 'O') and find(dx,dy,xs,ys, 'X')):
                    continue
                elif find(dx,dy,xs,ys, 'O'):
                    return "O won"
                elif find(dx,dy,xs,ys, 'X'):
                    return "X won"
            except IndexError:
                pass

    for l in v:
        for r in l:
            if r == '.':
                return "Game has not completed"

    return "Draw"


for case in xrange(1, T+1):
    print "Case #%d: %s" % (case, test())
    sys.stdout.flush()
