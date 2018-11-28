#!/usr/bin/env python

def part(ts,p,allow=False):
    a = ts//3
    d = ts - a*3
    if d == 0:
        l = [a,a,a]
    elif d == 1:
        l = [a,a,a+1]
    elif d == 2:
        l = [a,a+1,a+1]
    if p <= max(l):
        return True,False
    if allow:
        if d == 0 and a > 0:
            l = [a-1,a,a+1]
        elif d == 2:
            l = [a,a,a+2]
    if p <= max(l):
        return True,True
    return False,False


T = int(raw_input())
for t in range(T):
    L = [int(x) for x in raw_input().split()]
    N, S, p = L[:3]
    ts = L[3:]
    count = 0
    for s in ts:
        ret = part(s,p,S>0)
        if ret[0]:
            count += 1
            if ret[1]:
                S -= 1
    print 'Case #%d: %d' % (t+1,count)
