#!/usr/bin/env python

import sys

t = int(sys.stdin.readline())
for case in xrange(t):
    n = int(sys.stdin.readline())
    engines = [sys.stdin.readline().strip() for i in xrange(n)]
    q = int(sys.stdin.readline())
    queries = [sys.stdin.readline().strip() for i in xrange(q)]
    res = 0
    i = 0
    while i < q:
        res += 1
        last = {}
        for e in engines:
            last[e] = q
        for j in xrange(q-1, i-1, -1):
            last[queries[j]] = j
        i = max(last.itervalues())
    if res > 0:
        res -= 1
    print 'Case #%d: %d' % (case+1, res)
