#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys


T = int(sys.stdin.readline(), 10)

for t in xrange(1,T+1):
    line = sys.stdin.readline().strip().split()
    
    Smax = int(line[0], 10)
    Si = map(int, line[1])

    #print Si

    n = Si[0]
    answer = 0

    for i in xrange(1,Smax+1):
        #print i,Si[i],n,answer
        s = Si[i]
        #print i, n, i < n
        if i > n:
            #print "wtf"
            d = i - n
            answer += d
            n += d
        n += s

    print("Case #%d: %d" % (t, answer))


