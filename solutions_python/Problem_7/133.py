#!/usr/bin/env python

import sys
stream = sys.stdin
# stream = open("A-small.in", "r")
r = lambda: stream.readline().strip()

for case in range(0, int(r() ) ):
    
    (n, A, B, C, D, x0, y0, M) = [ int(i) for i in r().split() ]

    a = []
    X = x0
    Y = y0
    a.append( (X,Y) )
    for i in range( 1, n ):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        a.append( (X,Y) )

    count = 0
    for i1 in a:
        for i2 in a:
            if i1 == i2:
                continue
            for i3 in a:
                if i3 == i2 or i3 == i1:
                    continue
                if (i1[0] + i2[0] + i3[0]) % 3 == 0 and (i1[1] + i2[1] + i3[1]) % 3 == 0:
                    count += 1

    print "Case #%s: %s" % (case+1, count/6)

