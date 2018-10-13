#!/usr/bin/python

import sys

cases = int(sys.stdin.readline())

for casenum in range(1, cases+1):
    _, disk = map(int, sys.stdin.readline().split())
    files =  map(int, sys.stdin.readline().split())
    ans = 0
    files.sort()
    while len(files) > 0:
        if files[-1] + files[0] <= disk and len(files) > 1:
            files.pop(0)
        files.pop(-1)
        ans += 1
    print 'Case #{}: {}'.format(casenum, ans)
