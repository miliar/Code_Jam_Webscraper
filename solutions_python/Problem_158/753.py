#!/usr/bin/env python2

import sys

def readinput(f):
    test_cases = int(f.readline())
    for ncase in range(test_cases):
        x,r,c  = [int(c) for c in f.readline().split()]
        if x == 1:
            yield "GABRIEL"
        if x == 2:
            if r * c % 2 != 0:
                yield "RICHARD"
            else:
                yield "GABRIEL"
        if x == 3:
            if c == 1 or r == 1:
                yield "RICHARD"
            elif c * r % 3 == 0:
                yield "GABRIEL"
            else:
                yield "RICHARD"
        if x == 4:
            if (c >= 3 and r >= 3) and c * r % 4 == 0 and r * c >= 12:
                yield "GABRIEL"
            else:
                yield "RICHARD"

if __name__=="__main__":
    n = 1
    for case in readinput(sys.stdin):
        print "Case #%d: %s" % (n, case)
        n += 1
