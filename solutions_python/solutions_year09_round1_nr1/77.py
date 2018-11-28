#!/usr/bin/env python

import sys
from collections import defaultdict

T = int(sys.stdin.readline().strip())

bases = defaultdict(lambda: {})

def tobase(num, b):
    res = []
    while num:
        res.append(num % b)
        num /= b
    return res

def ishappy(num, b):
    if num in bases[b]:
        if bases[b] == None:
            return False
        else:
            return bases[b][num]
    else:
        sumsq = sum(i**2 for i in tobase(num, b))
        if sumsq == 1:
            res = True
        else:
            bases[b][num] = None
            res = ishappy(sumsq, b)
        bases[b][num] = res
        return res


for n in xrange(T):

    bs = [int(i) for i in sys.stdin.readline().strip().split()]

    num = 2
    while True:
        bad = False
        for b in bs:
            if not ishappy(num, b):
                bad = True
                break
        if not bad:
            break
        num += 1

    print "Case #%d:" % (n+1), num
