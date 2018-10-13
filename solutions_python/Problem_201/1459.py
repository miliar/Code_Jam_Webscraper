#!/usr/bin/env python

import sys
from operator import itemgetter

case = 0           
def count(n,k):
    if n<= k:
        print 'Case #'+str(case)+': 0 0'
        return 
    
    m_loc=0; ml=0
    d={str(n):1};i=0;j=1
    while j<k-i:
        p = {}
        for key,value in d.iteritems():
            t = int(key)
            m_loc = (t//2 if t%2 else t//2-1)
            x,y = str(m_loc),str(t-m_loc-1)
            p[x] = value+p.get(x,0)
            p[y] = value+p.get(y,0)
        i+=j;d=p;j*=2
    d = sorted(d.items(),key=itemgetter(0))
    s = 0
    for key, value in d[::-1]:
        if s+value <= k-1-i:
            s +=value
        else:
            temp = int(key)
            m_loc,ml = (temp//2 if temp%2 else temp//2-1),temp//2
            print 'Case #'+str(case)+': '+str(ml)+' '+str(m_loc)
            return
    

sys.stdin.readline()
for line in sys.stdin:
    case += 1;x,y=line.split()
    count(int(x),int(y))
    
