#!/usr/bin/python

T = int(raw_input())
for case in xrange(T):
    n, digits = raw_input().split()
    n = int(n)
    arr = map(int, digits)
    sz = n + 1
    arr = [sum(arr[:i+1]) for i in xrange(sz)]
    arr = [(i + 1) - e for i, e in enumerate(arr)]
    res = max(arr)
    res = max(res, 0)
    print 'Case #{}: {}'.format(case+1, res)
