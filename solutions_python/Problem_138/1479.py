#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bisect import bisect_left
T = int(raw_input())

for i in xrange(1,T+1):
    N = int(raw_input())
    nv = map(float, raw_input().split(" "))
    kv = map(float, raw_input().split(" "))
    assert len(nv) == len(kv) == N

    nv.sort()
    kv.sort()
    tmp = list(kv)

    dw = 0
    w = 0
    for a in nv[::-1]:
        pos = bisect_left(kv,a)
        if pos == len(kv):
            w += 1
            kv = kv[1:]
        else:
            kv = kv[:pos] + kv[pos+1:]

    kv = tmp
    for a in kv:
        pos = bisect_left(nv,a)
        if pos == len(nv):
            break
        else:
            dw += 1
            nv = nv[:pos] + nv[pos+1:]


    print "Case #%d: %d %d" % (i,dw,w)
