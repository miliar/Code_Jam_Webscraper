#!/usr/bin/python

import sys

C = int(sys.stdin.readline())

for i in range(1,C+1):
	N = int(sys.stdin.readline())
        A = map(int, sys.stdin.readline().split())

        ans = m = max(A)
        for j in xrange(1,m+1):
            sp = sum( (a-1)/j for a in A )
            ans = min(ans, j+sp)

	print 'Case #%d: %d' % (i, ans)

