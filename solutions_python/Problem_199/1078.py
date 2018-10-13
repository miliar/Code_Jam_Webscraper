from math import *
from fractions import Fraction as F
import sys
import os

si = sys.stdin
so = sys.stdout
se = sys.stderr

readline = raw_input
readargs = lambda : readline().split()
readints = lambda : map(int, readargs())

T = readints()[0]

for t in range(1, T + 1):
    patt, k = readargs()
    patt = map(lambda x : 0 if x == '+' else 1, patt)
    k = int(k)
    p = 0
    ans = 0
    print ('Case #%d:' % t),
    while p + k <= len(patt):
        if patt[p]:
            ans += 1
            for i in range(k):
                patt[p + i] = 1 - patt[p + i]
        p += 1
    # print filter(None, patt)
    if filter(None, patt):
        print 'IMPOSSIBLE'
    else:
        print ans

