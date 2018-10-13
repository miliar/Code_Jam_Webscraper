#!/usr/bin/env python

import sys
import math
inp = sys.stdin

def v(ll, lp, c):
    if lp < ll + 1:
        return set()

    mid = (ll  + (lp-ll)*0.5)
    top = (mid + (lp-mid)*0.5) 
    bot = (ll  + (mid-ll)*0.5)

    sl = v(ll, mid, c)
    sp = v(mid, lp, c)

    r = set([round(c**mid)])

    if len(sp) > len(sl):
        return r.union(sp)
    else:
        return r.union(sl)
    

def vals(l, p, c):
    v = []
    i = 1
    s = l*c
    while s < p:
        v.append(s)
        s = s*c
    return v

def go():
    l, p, c = map(int, inp.readline().split())
    v =  vals(l, p, c)
    #print v
    if l*c >= p:
        return 0

    return math.ceil(math.log(len(v)+1, 2))

    lp, ll = math.log(p, c), math.log(l, c)
    res = math.log((lp - ll),2)
    res = round(res+0.5)

    res = int(res)
    if res < 0:
        res = 0
    return int(res)

T = int(inp.readline())

for i in xrange(1, T+1):
    print 'Case #%d: %d' % (i, go())
