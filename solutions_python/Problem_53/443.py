#!/usr/bin/env python

import sys

try:
    w = int(sys.argv[2])
except:
    w = 8

def go(n, k):
    return (k+1) % 2**n == 0


if __name__ == '__main__':
    import fileinput

    inp = fileinput.input()
    t = int(inp.readline())


    for b in xrange(t):
        n, k = map(int, inp.readline().split())
        print "Case #%d: %s" % (b+1, ('ON' if go(n, k) else 'OFF' ) )

