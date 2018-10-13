#!/usr/bin/env python

import sys

tn = 1

for l in [l.strip() for l in sys.stdin.readlines()][1:]:
    n = l.split()
    a = int(n[0])
    b = int(n[1])
    c = len(n[0])

    p = {}
    cnt = 0

    for x in xrange(a, b):
        s = str(x)

        for i in range(c - 1):
            s = s[-1] + s[:-1]
            y = int(s)

            if x < y and y <= b:
                cnt += 1
                #if x in p:
                #    p[x].append(y)
                #else:
                #    p[x] = [y]

    #for k in sorted(p.keys()):
    #    print k, p[k]
    #    s += len(p[k])

    print 'Case #{0}: {1}'.format(tn, cnt)
    tn += 1
