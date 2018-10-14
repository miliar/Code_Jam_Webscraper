#!/usr/bin/env python

t = int(raw_input())

for tc in xrange(1, t+1):
    a, b = raw_input().split()
    n, m = int(a), int(b)
    l = len(a)
    seen = set()
    cnt = 0
    for x in xrange(n, m+1):
        for p in xrange(1, l):
            s = str(x)
            y = int(s[p:] + s[:p])
            if (x, y) in seen:
                continue
            seen.add((x, y))
            if x == y:
                continue
            if n <= x < y <= m:
                cnt = cnt + 1
    print "Case #%s: %s" % (tc, cnt)
