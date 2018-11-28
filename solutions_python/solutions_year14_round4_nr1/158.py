#!/usr/bin/python2
# coding: utf-8

from sys import stdin

T = int(stdin.readline().rstrip())

for ct in range(T):
    fnum, dcap = map(int, stdin.readline().split())
    fsizes = sorted(map(int, stdin.readline().split()))
    ans = 0
    while fsizes:
        ans += 1
        if len(fsizes) > 1 and fsizes[-1] + fsizes[0] <= dcap:
            fsizes = fsizes[1:-1]
        else:
            fsizes = fsizes[:-1]

    print 'Case #{0}: {1}'.format(ct + 1, ans)
