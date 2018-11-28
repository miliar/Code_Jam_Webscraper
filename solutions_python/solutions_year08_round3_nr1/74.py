#!/usr/bin/env python

from sys import stdin

N = int(stdin.readline())

for case in xrange(N):
    p, k, l = [int(x) for x in 
               stdin.readline().strip().split(' ')]
    
    freqs = [int(x) for x in 
             stdin.readline().strip().split(' ')]

    for i in xrange(l):
        freqs[i] = (freqs[i], i)

    freqs.sort()
    freqs.reverse()

    sum = 0
    i = 0
    pos = 1
    for (f,v) in freqs:
        sum += pos * f
        i += 1
        i %= k
        if i == 0:
            pos += 1

    print "Case #%d: %d" % (case+1, sum)
