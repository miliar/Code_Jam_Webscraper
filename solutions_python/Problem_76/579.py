# -*- coding: utf-8 -*-
from itertools import combinations

t = int(raw_input())

def patrick(li):
    res = 0
    for e in li:
        res ^= e
    return res

def solve(li):
    li.sort(reverse=True)
    res = 0
    for i in xrange(len(li) - 1, 0, -1):
        bases = combinations(li, i)
        for basis in bases:
            remainder = li[:]
            for e in basis:
                remainder.remove(e)
            if patrick(basis) == patrick(remainder):
                tmp = max(sum(basis), sum(remainder))
                if res < tmp:
                    res = tmp
                    return res
    return res

for i in xrange(1, t + 1):
    n = int(raw_input())
    cs = raw_input().split(' ')
    cs = [int(e) for e in cs if e]
    res = solve(cs)
    res = str(res) if res else 'NO'
    print 'Case #%d: %s' % (i, res)
