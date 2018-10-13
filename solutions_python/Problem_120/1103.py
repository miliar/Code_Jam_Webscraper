#!/usr/bin/pypy

import sys
import math



def fcmp(a, b, precision = .0000000000001):
    """
    Compares floating points with a specified precision
    returns a number RET such that:
        0 == RET iff a == b
        0 <  RET iff a < b
        0 >  RET iff a > b
    """
    if abs(a - b) < precision: return 0
    else: return cmp(a, b)

def realbinsearch(low, high, test):
    """
    Runs a binary search across the range of real numbers: [low, high] and
    returns the first value that passes test(x)

    test -- must take a float X and return a value, RET, such that
            0 == RET iff X is the desired value
            0 <  RET iff X is higher than the desired value
            0 >  RET iff X is lower than the desired value
    """
    left, right = float(low), float(high)
    prec = .0000000000001
    while fcmp(left, right, prec) < 0:
        mid = (left + right) * 0.5
        t = test(mid)
        if t == 0: break
        elif t > 0: right = mid - prec
        else: left = mid + prec
    return mid

def ring_area(r):
    return (r * 2) + 1

def solve(r, t):
    paint_used = ring_area(r)
    rings_painted = 0
    while paint_used <= t:
        r += 2
        rings_painted += 1
        paint_used += ring_area(r)
    return rings_painted



T = int(sys.stdin.readline())
for i in range(1,T+1):
    r, t = [int(s) for s in sys.stdin.readline().split()]
    print "Case #%d: %s" % (i, solve(r, t))

