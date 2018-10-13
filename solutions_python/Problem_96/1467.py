#! /usr/bin/env python
#! -*- coding: utf-8 -*-

import sys

cases = sys.stdin.readline()
case = 1
for line in sys.stdin:
    l = line[:-1].split(' ')
    num, sup, ctr, scores = int(l[0]), int(l[1]), int(l[2]), [int(i) for i in l[3:]]
    ans = 0
    #print num, sup, ctr, scores
    for s in scores:
        if ctr == 1:
            if s >= 1: ans += 1
        elif s >= (ctr-1)*3+1:
            ans += 1
        elif s >= (ctr-1)*3-1 and sup: 
            ans += 1
            sup -= 1

    print "Case #%d: %s" % (case, ans)
    case += 1
