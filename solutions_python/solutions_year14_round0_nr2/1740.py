#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import collections

fin = sys.stdin
T = int(fin.readline())

for case in range(1, T + 1):
    cfx = list(map(float,fin.readline().split()))

    t = 0
    v = 2

    while True:
        timeNewFact = cfx[0] / v
        timeNextDest = timeNewFact + cfx[2]/(v+cfx[1])
        timeDest = cfx[2] / v
        
        if timeDest <= timeNextDest:
            t = t + timeDest
            break
        else:
            t = t + timeNewFact
            v = v + cfx[1]


    print("Case #%d: %.7f" % (case, t))
    