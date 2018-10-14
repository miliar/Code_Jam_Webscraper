#! /usr/bin/env python

from sys import stdin

ntest = input()

for test in range(ntest):
    x, s, r, t, n = [int(i) for i in stdin.readline().strip().split()]
    ways = []
    last = 0
    
    for way in range(n):
        b, e, w = [int(i) for i in stdin.readline().strip().split()]
        if last != b:
            ways.append((0, b-last))
        ways.append((w, e-b))
        last = e
        
    if last != x:
        ways.append((0, x-last))
    
    ways.sort()
    
    seconds = 0.
    t = t * 1.
    
    for speed, length in ways:
        if t>0:
            if t*(speed+r)>length:
                #corro sempre
                time = (1.0 * length) / (speed+r)
                seconds += time
                t -= time
            else:
                seconds += t + (1.0 * length - (speed+r) * t) / (speed+s)
                t = 0
        else:
            #cammino sempre
            seconds += (1.0 * length) / (speed+s)
            
    print "Case #%d: %.9f" % (test+1, seconds)