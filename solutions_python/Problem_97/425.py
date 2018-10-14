# -*- coding: utf-8 -*-

t = int(raw_input())

for i in xrange(1, t+1):
    res = 0
    a, b = [int(e) for e in raw_input().split(' ')]
    for n in xrange(a, b+1):
        ns = str(n)
        c = set()
        for k in xrange(1, len(ns)):
            m = int(ns[k:] + ns[:k])
            if a <= n < m <= b:
                c.add((n, m))
        res += len(c)
    print 'Case #%d: %d' % (i, res)
