#!/usr/bin/env python
from sys import stdin

tn = int(stdin.readline())
for ti in xrange(tn):
	s, k = stdin.readline().split()
        s = map(lambda x: 1 if x == '+' else 0, s)
        k = int(k)
        n = len(s)
        c = 1
        r = 0
        cn = [0 for i in xrange(n+1)]
        for i in xrange(n):
            if cn[i]:
                c = 1-c
            if s[i] != c:
                if i > n-k:
                    r = 'IMPOSSIBLE'
                    break
                c = 1-c
                r += 1
                cn[i+k] = 1
	print 'Case #{0}:'.format(ti+1), r
