#!/usr/bin/env python
import sys
from collections import defaultdict

def is_recycled(i, j):
    s = str(i)
    t = str(j)
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if s[i:]+s[:i] == t:
            return True
    return False

test_size = int(sys.stdin.readline())

for x in range(1, test_size+1):
    A, B = sys.stdin.readline().strip().split(" ",1)
    A, B = int(A), int(B)
    y = 0
    for i in xrange(A,B):
        for j in xrange(i+1, B+1):
            if is_recycled(i,j):
                y += 1
    print "Case #%d: %s" % (x, y)

