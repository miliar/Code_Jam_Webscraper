#!/usr/bin/env python

import sys

def solve(audience):
    nstand = 0
    friends = 0
    for i,s in enumerate(audience):
        if nstand < i:
            friends += (i - nstand)
            nstand += (i - nstand)
        nstand += s
    return friends

if __name__ == "__main__":
    infile = sys.argv[1]
    lines = [l.strip() for l in open(infile).readlines()]

    T = int(lines.pop(0))

    for t in xrange(T):
        smax, audience = lines.pop(0).split(' ')
        smax = int(smax)

        audience = map(int, audience)
        print "Case #%d: %d" % (t+1, solve(audience))
