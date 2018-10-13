#!/usr/bin/env python

def cnt(r, t):
    n = int((((2*r-1)**2 + 8*t)**0.5 - (2*r-1))/4)
    n = n + 1
    while 2*n*r + 2*n*n - n > t: n -= 1
    return n

T = int(raw_input())
for i in range(T):
    r, t = [int(j) for j in raw_input().split()]
    print "Case #%d: %d" % (i+1, cnt(r, t))
