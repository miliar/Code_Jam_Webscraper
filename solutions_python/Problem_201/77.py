#!/usr/bin/env python

import sys
ls = sys.stdin.readlines()[1:]
C = 1
for l in ls:
    n, k = [int(x) for x in l.split()]
    a = {n: 1}
    i = 0
    while i < k:
        x = max(a.keys())
        y = a[x]
        del a[x]

        for s in (x/2, x/2 - 1 + (x % 2)):
            if s not in a:
                a[s] = 0
            a[s] += y
        i += y
    print "Case #%d: %d %d" % (C, x/2, x/2 - 1 + (x % 2))
    C += 1
