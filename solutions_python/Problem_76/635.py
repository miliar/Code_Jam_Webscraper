# -*- coding: utf-8 -*-
#TLE
from itertools import combinations
from operator import xor

T = input()

def ssum(l):
    return reduce(xor, l)

def doit():
    maxx = -1
    N = int(raw_input())
    numbers = map(int, raw_input().split())
    indexes = range(N)
    for i in xrange(1, N):
        for comb in combinations(indexes, i):
            s = set(comb)
            l1 = []
            l2 = []
            for v in indexes:
                if v in s:
                    l1.append(numbers[v])
                else:
                    l2.append(numbers[v])
            if ssum(l1) == ssum(l2):
                maxx = max(maxx, sum(l1), sum(l2))
    return 'NO' if maxx == -1 else maxx

for t in xrange(1, T+1):
    ans = doit()
    print 'Case #%d: %s' % (t, str(ans))