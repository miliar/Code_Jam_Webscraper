#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

T = int(sys.stdin.readline())
for i in range(1, T+1):
    l = sys.stdin.readline()
    cols = l.split(None)
    N = int(cols[0])
    S = int(cols[1])
    p = int(cols[2])
    scores = [int(x) for x in cols[3:]]
    scores_max = [(x, (x/3+1 if x % 3 != 0 else (x/3 if x >= 2 else x))) for x in scores]

    over = [x for x in scores_max if x[1] >= p]
    pot = [x for x in scores_max if x[0] >= 2 and x[1] == p-1 and x[0] % 3 != 1]
    print "Case #%d:" % i, len(over) + min(S, len(pot))
