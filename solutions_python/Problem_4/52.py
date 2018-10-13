#/usr/bin/env python

import sys

readline = lambda : sys.stdin.readline()

N = int(readline())

for n in range(N):
    T = int(readline())
    A = map(int, readline().split())
    B = map(int, readline().split())
    A.sort()
    B.sort()
    B = list(reversed(B))
    s = 0
    for a,b in zip(A, B):
        s += a * b
    print "Case #%d: %d" % (n+1, s)


