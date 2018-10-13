#!/usr/bin/python

import sys

cases = int(sys.stdin.readline())

for casenum in range(1, cases+1):
    sys.stdin.readline()
    ar = map(int, sys.stdin.readline().split())
    order = sorted(ar)
    ans = 0
    for i in order:
        index = ar.index(i)
        ans += min(index, len(ar) - index - 1)
        ar.remove(i)
    print 'Case #{}: {}'.format(casenum, ans)
