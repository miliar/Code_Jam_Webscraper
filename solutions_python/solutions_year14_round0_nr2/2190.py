#!/usr/bin/env python

import sys
import itertools


def solve(C, F, X):
    cookies = 0
    performance = 2
    t = 0.0
    while cookies <= X:
        if X <= C:
            t = t + X / performance
            cookies = X
            break
        else:
            nowConsumed = X / performance
            nextConsumed = C / performance + X / (performance + F)
            if nowConsumed > nextConsumed:
                consumed = C / performance
                t = t + consumed
                performance = performance + F
            else:
                consumed = X / performance
                t = t + consumed
                cookies = X
                break
        #print "t: %f, cookies: %f, performance: %f" % (t, cookies, performance)
    return t


filename = sys.argv[1]

inp = open(filename.strip())
lines = inp.readlines()

i = 1
for line in lines[1:]:
    (C, F, X) = map(lambda i: float(i), line.strip().split(" "))
    print "Case #%d: %s" % (i, solve(C, F, X))
    i += 1

