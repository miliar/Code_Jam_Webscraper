#!/usr/bin/python

import sys


def debug(msg):
#    return
    sys.stderr.write("\x1b[33;1m"+str(msg)+"\x1b[0m\n")

nb = int(raw_input())

R = "RICHARD"
G = "GABRIEL"
U = "UNKNOWN"


for case in xrange(1, nb+1):
    x, r, c = [ int(i) for i in raw_input().split() ]

    W = U
    for i in xrange(2):
        if x == 1:
            W = G
            break

        if x > r and x > c:
            W = R
            break

        if (r * c) % x != 0:
            W = R
            break

        if (r == 1 or c == 1) and x > 2:
            W = R
            break

        if x == 2 or x == 3:
            W = G
            break


        if x == 4 and r == 4 and (c == 3 or c == 4):
            W = G
            break

        if x == 4 and r == 4 and c == 2:
            W = R
            break

        r, c = c, r
    print "Case #%d: %s" % (case, W)

