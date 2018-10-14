#!/usr/bin/env python
import sys
import math


def solve(r, t):
    n = int((math.sqrt(4 * r**2 - 4 * r + 8 * t + 1) - 2 * r + 1) / 4) + 2
    # lazily account for off-by-one errors
    while True:
        paint = 2 * n**2 + 2 * n * r - n
        if paint > t:
            n -= 1
        else:
            return n

if __name__ == '__main__':
    with open(sys.argv[1], 'rU') as fin, open(sys.argv[2], 'w') as fout:
        T = int(fin.readline())
        for case in xrange(1, T+1):
            print "Case #{0}:".format(case),

            r, t = map(int, fin.readline().split())

            soln = solve(r, t)
            print soln
            print >> fout, "Case #{0}: {1}".format(case, soln)
