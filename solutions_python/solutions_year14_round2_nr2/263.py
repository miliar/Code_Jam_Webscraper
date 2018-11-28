#!/usr/bin/python
import sys

def solve(A, B, K):
    total = 0
    for i in xrange(A):
        for j in xrange(B):
            if i&j < K:
                total += 1
    return total

T = int(sys.stdin.readline())
for i in xrange(T):
    print "Case #%d:" % (i+1),
    A, B, K = map(int, sys.stdin.readline().strip().split(" "))
    print solve(A, B, K)
