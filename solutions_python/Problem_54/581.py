#!/usr/local/bin/python2.6
import sys
from fractions import gcd

c = int(sys.stdin.readline())
for _ in range(1,c+1):
    t = map(int, sys.stdin.readline().split())
    n = t.pop(0)
    d = 0
    for i in range(1,n):
        d = gcd(d, abs(t[i]-t[0]))
    t[0] %= d
    if t[0] != 0:
        t[0] = d - t[0]
    print "Case #%d: %d" % (_,t[0])
