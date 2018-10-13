#!/usr/bin/env python

import sys
from itertools import cycle, islice

cnt_max = int(sys.stdin.readline())
for cnt in xrange(1, cnt_max+1):
    ans = 0
    A, B = map(int, sys.stdin.readline().rstrip().split())
    l = len(str(A))
    for n in xrange(A, B+1):
        if A <= n and n < B:
            nn_str = str(n)*2
            for m in set([int(nn_str[i:i+l]) for i in xrange(1, l)]):
                if n < m and m <= B:
                    ans += 1
    print "Case #%d: %d" % (cnt, ans)
