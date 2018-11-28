#!/usr/bin/env python
# -*- coding: utf-8 -*-

t = int(raw_input())
for i in xrange(t):
    cols = raw_input().strip().split(" ")
    n = int(cols[0]) # googlers
    s = int(cols[1]) # surprising triplets
    p = int(cols[2]) # minimum best score
    t = (int(i) for i in cols[3:]) # total scores

    boundary_non_surpr = p * 3 - 2
    boundary_surpr = max(p * 3 - 4, 1)
    non_surpr = 0
    surpr = 0
    for ti in t:
        if ti >= boundary_non_surpr:
            non_surpr += 1
        elif ti >= boundary_surpr:
            surpr += 1
    result = non_surpr + min(surpr, s)
    print "Case #{0}: {1}".format(i+1, result)
