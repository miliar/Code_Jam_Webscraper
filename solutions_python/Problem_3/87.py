#!/usr/bin/env python

from __future__ import division

import sys
import math
import itertools

def area(x, y, R):
    if x >= R or y >= R:
        return 0
    dist = math.hypot(x, y)
    if dist >= R:
        return 0
    y1 = math.sqrt(R**2 - x**2)
    x1 = math.sqrt(R**2 - y**2)
    res = abs(x1 - x) * abs(y1 - y)
    len = math.hypot(x - x1, y - y1)
    alfa = 2 * math.asin(len / (2 * R))
    res += alfa * R**2
    res -= math.sin(alfa) * R**2
    return res * .5

def solve(f, R, t, r, g):
    free = 0
    total = math.pi * R**2
    R -= f + t
    g -= 2*f
    r += f
    w = g + 2*r
    for i in itertools.count():
        x0 = i*w + r
        x1 = x0 + g
        if x0 >= R:
            break
        for j in itertools.count():
            y0 = j*w + r
            y1 = y0 + g
            dist0 = math.hypot(x0, y0)
            if dist0 >= R:
                break
            dist1 = math.hypot(x1, y1)
            if dist1 <= R:
                free += g**2
            else:
                a = 0
                a += area(x0, y0, R)
                a -= area(x1, y0, R)
                a -= area(x0, y1, R)
                a += area(x1, y1, R)
                assert a <= g**2
                free += a
    return (total - 4*free) / total

cases = int(sys.stdin.readline())
for case in xrange(cases):
    f, R, t, r, g = [float(x) for x in sys.stdin.readline().split()]
    print 'Case #%d: %.10f' % (case+1, solve(f, R, t, r, g))
