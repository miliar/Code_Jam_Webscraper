from __future__ import print_function, division
import sys
import array
import re
from heapq import heappush, heappop
from fractions import gcd
from future_builtins import filter, map, zip
#import numpy as np
DD=print

TOTAL = int(raw_input())
for case in xrange(1,TOTAL+1):
    X,S,R,t,N=map(int, raw_input().split())
    T=0
    W=[]
    x=X
    for n in xrange(N):
        b,e,w=map(int, raw_input().split())
        W.append((w+S,e-b))
        x-=e-b
    W.append((S,x))

    W=sorted(W)
    
    d=R-S
    for s,l in W:
        #print(s,l,T,t)
        if t>0:
            if l/(s+d) < t:
                t-=l/(s+d)
                T+=l/(s+d)
                continue
            else:
                T+=t
                l-=(s+d)*t
                t=0
        T+=l/s
    print('Case #{0}:'.format(case), T)
