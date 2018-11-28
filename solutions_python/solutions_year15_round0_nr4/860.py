#!/usr/bin/python

import sys


def readints(f):
    return [int(s) for s in f.readline().split()]


def readint(f):
    return int(f.readline())


def solve(x, r, c):
    if x == 1:
        return "GABRIEL"
    elif x >= 7 or (r * c) % x > 0:
        return "RICHARD"

    if x == 2:
        return "GABRIEL"
    if x == 3:
        if r == 1 or c == 1:
            return "RICHARD"
        return "GABRIEL"
    if x == 4:
        if r * c == 12 or r * c == 16:
            return "GABRIEL"

    return "RICHARD"

if __name__ == "__main__":
    f = open(sys.argv[1], "r")

    numCases = readint(f)
    for i in xrange(numCases):
        x, r, c = readints(f)
        print "Case #%d: %s" % (i + 1, solve(x, r, c))
