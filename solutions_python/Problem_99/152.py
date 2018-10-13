#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
T = int(sys.stdin.readline())
for t in range(1, T+1):
    A, B = tuple([int(x) for x in sys.stdin.readline().split(None)])
    problist = [float(x) for x in sys.stdin.readline().split(None)]
    mistype_prob = 0.0
    # give up immediately
    min_cost = B + 2
    for i in range(A):
        # mistyped the i-th character
        mistype_prob += (1.0 - mistype_prob) * (1.0 - problist[i])
        # expectation of # remaining types
        exp = mistype_prob * (B + 1) + (B - i) + (A - i - 1)
        if exp < min_cost:
            min_cost = exp
    print "Case #%d: %f" % (t, min_cost)
