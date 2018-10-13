#! /usr/bin/env python
# vim: set et ts=4 sw=4 ci cino=(0:
import sys
import os
import math

def main():
    f = open(sys.argv[1])
    ntest = int(f.readline().strip())

    for t in xrange(ntest):
        l = [ int(x) for x in f.readline().strip().split() ]   
        if len(l) != 3:
            print "Error ", l
            sys.exit(1)
        low = l[0]
        high = l[1]
        c = l[2]

        nr = 0
        while (low * c) < high:
            nr += 1
            fa = math.sqrt(float(high)/float(low))
            h1 = int(math.ceil(float(high)/fa))
            high = h1

        print "Case #%d: %d" % (t+1, nr)

if __name__ == "__main__":
    main()

