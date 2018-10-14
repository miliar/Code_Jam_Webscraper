#!/usr/bin/env python

import sys
T = int(sys.stdin.readline()) # test case count

for case in range(T):
    xs = []
    ys = []
    n = int(sys.stdin.readline())
    xs = map(int, sys.stdin.readline().split())
    ys = map(int, sys.stdin.readline().split())

    xs.sort()
    ys.sort()
    ys.reverse()

    zs = []
    for i in range(0,len(xs)):
        zs.append(xs[i]*ys[i])

    print "Case #"+str(case+1)+":",sum(zs)
