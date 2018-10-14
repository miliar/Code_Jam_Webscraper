# -*- coding: utf-8 -*-

from bisect import bisect, bisect_left

t = int(raw_input())

def dwar(naomi, ken):
    res = 0
    for i in xrange(len(naomi)):
        if naomi[0] < ken[0]:
            naomi.pop(0)
            ken.pop(-1)
        else:
            naomi.pop(0)
            ken.pop(0)
            res += 1
    return res

def war(naomi, ken):
    res = 0 
    for e in naomi:
        h = bisect(ken, e)
        if len(ken) <= h:
            h = 0
        k = ken.pop(h)
        if k < e:
            res += 1
    return res

for i in xrange(1, t+1):
    n = int(raw_input())
    naomi = [float(e) for e in raw_input().split()]
    ken = [float(e) for e in raw_input().split()]
    naomi.sort()
    ken.sort()
    print 'Case #%d:' % i, dwar(naomi[:], ken[:]), war(naomi, ken)
