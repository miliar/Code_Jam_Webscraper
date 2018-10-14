#!/usr/bin/python

import re
from sys import stdin

def how_many_recycled(a, b):
    r = 0
    for i in xrange(a, b):
        r += how_many_recycled_le(i, b)
    return r

def how_many_recycled_le(i, b):
    si = str(i)
    rcyc = set([])
    for j in range(1, len(si)):
        sri = si[j:] + si[:j]
        if sri[0] == '0': continue
        ri = int(sri)
        if i < ri <= b: rcyc.add(ri)
    return len(rcyc)

ncases = int(stdin.readline().strip())

for i, line in enumerate(stdin.xreadlines()):
    a, b = re.split(' +', line.strip())
    a, b = int(a), int(b)
    print("Case #%i: %i" % (i+1, how_many_recycled(a, b)))
