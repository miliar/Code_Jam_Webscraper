from __future__ import division
from math import *

T = int(raw_input())
for case in xrange(T):
    L, P, C = map(int, raw_input().split(' '))
    try:
        ans = int(ceil(log(log(P/L)/log(C))/log(2)))
        if ans < 0:
            ans = 0
    except ValueError, e:
        ans = 0
    print "Case #%s: %s" %(case+1, ans)
