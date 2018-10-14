#!/usr/bin/env python2

import os, sys


def solve ( C, F, X ):
    crate = 2.0
    cookiecnt = 0
    t = 0

    while True:
        t1 = X / crate
        t2 = (C / crate) + (X/(crate+F))

        # check if reachable without a new farm:
        if t1 < t2:
            return t1 + t

        # if not buy a farm and continue:
        t += C/crate
        crate += F
        cookiecnt = 0

    return t


fd = sys.stdin

line = fd.readline()
sets = int( line )+1

for case in range(1, sets):
    C, F, X = ( float( x ) for x in fd.readline().split() )
    nline = solve( C, F, X )
    print "Case #%s: %s" % (case, nline)

fd.close()
