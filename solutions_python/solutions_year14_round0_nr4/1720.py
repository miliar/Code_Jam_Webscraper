#!/usr/bin/python
import sys

# Deceitful War

def next_higher(chosen, avail):
    for c in avail:
        if c > chosen:
            return c
    return avail[0]

def war(naomi, ken):
    npoints = 0
    for n in reversed(naomi):
        k = next_higher(n, ken)
        if n > k:
            npoints += 1
        ken.remove(k)
    return npoints

def deceitwar(naomi, ken):
    pnaomi = 0
    while len(naomi) > 0:
        if naomi[0] > ken[0]:
            pnaomi += 1
            naomi.pop(0)
            ken.pop(0)
        else:
            naomi.pop(0)
            ken.pop()
    return pnaomi

lines = [l.rstrip() for l in sys.stdin.readlines()]
for x in xrange(int(lines.pop(0))):
    naomi = sorted([float(i) for i in lines[x*3+1].split(' ')])
    ken = sorted([float(i) for i in lines[x*3+2].split(' ')])
    print("Case #%u: %u %u" % (x + 1, deceitwar(naomi[:], ken[:]), war(naomi[:], ken[:])))
