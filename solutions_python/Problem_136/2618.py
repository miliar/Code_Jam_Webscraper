#!/usr/bin/python

import sys

def read_obj(cls):
    return cls(sys.stdin.readline().strip())

def read_obj_list(cls):
    return map(cls, sys.stdin.readline().strip().split())

def solve():
    t = read_obj(int)
    for i in xrange(1, t + 1):
        c, f, x = read_obj_list(float)
        best = x / 2
        cost = 0
        for j in xrange(1, int(x) + 1):
            cost += c / (2 + (j - 1) * f)
            best = min(cost + x / (2 + j * f), best)
        print "Case #%d: %.7f" % (i, best)

if __name__ == "__main__":
    solve()
