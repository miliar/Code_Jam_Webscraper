#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import fractions

def solve(maap, H, W, D):
    # distances to reflections
    distup = None
    distleft = None
    assert len(maap) == H
    for ypos,line in enumerate(maap):
        assert len(line) == W
        xpos = line.find('X')
        if xpos != -1:
            distup = (ypos - 1) * 2 + 1
            distleft = (xpos - 1) * 2 + 1
            break
    assert distup is not None
    assert distleft is not None
    distdown = H * 2 - distup - 4
    distright = W * 2 - distleft - 4
    assert distup > 0
    assert distdown > 0
    assert distleft > 0
    assert distright > 0
    #print >>sys.stderr, distup, distdown, distleft, distright, H, W, D

    # find leftest possible point
    used_directions = set()

    def update_used_directions(x, y):
        if x != 0 or y != 0:
            gcd = abs(fractions.gcd(x, y))
            used_directions.add((x / gcd, y / gcd))

    def far(x, y):
        return x*x + y*y > D*D

    def explore_vert(curx, cury, dy, ndy):
        while not far(curx, cury):
            #print >> sys.stderr, curx, cury
            update_used_directions(curx, cury)
            cury += dy
            dy, ndy = ndy, dy
        #print >>sys.stderr, 'bad: {x}, {y}'.format(x=curx, y=cury)

    def explore_hor(curx, cury, dx, ndx):
        while not far(curx, cury):
            explore_vert(curx, cury, distdown, distup)
            explore_vert(curx, cury, -distup, -distdown)
            curx += dx
            dx, ndx = ndx, dx
        #print >>sys.stderr, 'bad: {x}, {y}'.format(x=curx, y=cury)

    explore_hor(0, 0, distleft, distright)
    explore_hor(0, 0, -distright, -distleft)
    #print >>sys.stderr, used_directions
    return len(used_directions)

ilines = sys.stdin.xreadlines()
numproblems = int(next(ilines))
for i in xrange(numproblems):
    line = next(ilines)
    H, W, D = map(int, line.strip().split())
    maap = [next(ilines).strip() for _ in xrange(H)]
    print 'Case #{i}: {res}'.format(i=i+1, res=solve(maap, H, W, D))
