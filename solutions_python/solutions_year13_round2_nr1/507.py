#!/usr/bin/python
from sys import stderr
from collections import deque

def gcd(i, j): return i == 0 and j or gcd(j % i, i)

for t in xrange(int(raw_input())):
    A, N = map(int, raw_input().split())
    m = map(int, raw_input().split())
    m.sort()

    c = 0
    for i in xrange(len(m)):
        c0 = c
        if A > m[i]:
            A += m[i]
        else:
            while A <= m[i]:
                c0 += 1
                A += A - 1
                if c0 - c >= len(m) - i: c0 = 0; break
            if c0 == 0: c += len(m) - i; break
            else:
                A += m[i]
                c = c0

    print "Case #%d: %d" %(t + 1, c)
