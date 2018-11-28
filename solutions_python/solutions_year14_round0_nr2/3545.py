#!/usr/bin/env python
#-*- coding: utf-8 -*-

def solve (C, F, X):
    lim, init, r, ret = int (X + 5), 0, 2.0, X / 2.0
    for n in range (0, lim):
        ret = min (ret, init + X / (F * n + r))
        init += (C / (r + n * F))
    return ret

T = int (raw_input ())
for t in range (1, T + 1):
    C, F, X = [float (i) for i in raw_input ().split ()]
    ret = solve (C, F, X)
    print "Case #{0}: {1:0.7f}".format (t, ret)

