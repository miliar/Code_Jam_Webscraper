#!/usr/bin/env python

import sys
ls = sys.stdin.readlines()
n = int(ls[0])
ls = ls[1:]
for C in range(n):
    num, p = [int(x) for x in ls[0].split()]
    ls = ls[1:]
    req = [float(x) for x in ls[0].split()]
    ls = ls[1:]
    ps = []
    for i, l in enumerate(ls[:num]):
        s = [float(x)/req[i] for x in l.split()]

        s.sort()
        ps.append(s)
    ls = ls[num:]
    ans = 0
    idxs = [0] * num
    while max(idxs) < p:
        lo = 0
        hi = 1000000000
        minidx = 0
        minv = 1000000000
        for i, idx in enumerate(idxs):
            if ps[i][idx] < minv:
                minv = ps[i][idx]
                minidx = i
            lo = max(lo, int(ps[i][idx]/1.1 + 1 - 0.000000001))
            hi = min(hi, int(ps[i][idx]/0.9 + 0.000000001))
        if lo <= hi:
            ans += 1
            for i in range(len(idxs)):
                idxs[i] += 1
        else:
            idxs[minidx] += 1
            
    print "Case #%d: %d" % (C + 1, ans)
