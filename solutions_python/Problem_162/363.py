from sys import stdin
import re
import operator
import bisect
import sys
import random
from collections import defaultdict
from functools import reduce # Valid in Python 2.6+, required in Python 3
import operator
from fractions import gcd

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

d = {"0":0}

for i in xrange(1, 10**6+1):
    s, p = str(i), str(i-1)
    r = s[::-1]
    d[s] = d[p]+1
    if r in d:
        d[s] = min(d[s], d[r]+1)

cases = int(stdin.next().strip())
for case in range(1, cases+1):
    N = str(stdin.next().strip())
    print 'Case #%d: %d' % (case, d[N])



    

