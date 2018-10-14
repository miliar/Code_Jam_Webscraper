#! /usr/bin/env python
# vim: set et ts=4 sw=4 ci cino=(0:
import sys
import os

def main():
    f = open(sys.argv[1])
    ntest = int(f.readline().strip())

    for t in xrange(ntest):
        l = [ int(x) for x in f.readline().strip().split() ]
        if len(l) != 4:
            print "Error ", l
            sys.exit(1)
        nchicks = l[0]
        minchicks = l[1]
        barn = l[2]
        timel = l[3]

        clocks = [ int(x) for x in f.readline().strip().split() ]
        cspeeds = [ int(x) for x in f.readline().strip().split() ]

        if len(clocks) != nchicks or len(cspeeds) != nchicks:
            print "Error 1"
            sys.exit(1)

        if minchicks == 0:
            print "Case #%d: 0" % (t+1)
            continue

        nreached = 0
        nslow = 0
        nswaps = 0
        for i in xrange(nchicks-1, -1, -1):
            if (cspeeds[i] * timel) >= (barn - clocks[i]):
                nswaps += nslow
                nreached += 1
            else:
                nslow += 1

            if nreached >= minchicks:
                break

        if nreached >= minchicks:
            print "Case #%d: %d" % (t+1, nswaps)
        else:
            print "Case #%d: IMPOSSIBLE" % (t+1)

if __name__ == "__main__":
    main()

