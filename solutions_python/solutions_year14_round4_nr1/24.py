#!/usr/bin/env python

def solve(N, X, S):
    num = [0] * (X + 1)
    for s in S:
        num[s] += 1
    res = 0
    for x in reversed(xrange(X + 1)):
        while num[x]:
            res += 1
            num[x] -= 1
            for y in reversed(xrange(X - x + 1)):
                if num[y]:
                    num[y] -= 1
                    break
    return res

T = int(raw_input())
for x in xrange(1, T + 1):
    N, X = map(int, raw_input().split())
    S = map(int, raw_input().split())
    print 'Case #%d: %s' % (x, solve(N, X, S))
