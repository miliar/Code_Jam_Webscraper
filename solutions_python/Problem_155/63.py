#!/usr/bin/python

import sys

C = int(sys.stdin.readline())

for i in range(1,C+1):
	s = sys.stdin.readline().split()
	N = int(s[0])
        A = map(int, s[1].strip())
        r = 0
        s = 0
        for (j,c) in enumerate(A):
            if c>0 and s+r<j:
                r = j - s
            s += c
	print 'Case #%d: %d' % (i, r)
