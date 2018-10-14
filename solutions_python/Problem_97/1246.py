#!/usr/bin/env python
import sys

def rotate(a):
    s = set([a])
    for i in range(1, len(str(a))):
        t = int( str(a)[i:] + str(a)[0:i] )
        if t not in s:
            s.add(t)
            yield int( str(a)[i:] + str(a)[0:i] )

n = int(raw_input())
for t in range(n):
    res = 0
    (a, b) = map(int, raw_input().split(' '))
    for i in range(a, b):
        for k in rotate(i):
            if a <= k <= b and k > i:
                res += 1
    print "Case #%d: %d" % ((t+1), res)

