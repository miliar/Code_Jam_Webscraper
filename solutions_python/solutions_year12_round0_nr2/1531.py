#!/usr/bin/env python

import sys
from math import *

f = open(sys.argv[1])

n = int(f.readline())

for i in range(n):
    a = f.readline().split()
    N, S, P = int(a[0]),int(a[1]), int(a[2])

    a = map(int,a[3:])
    count =0
    for j in range(N):
        if a[j]<P:
            continue
        value = ceil(a[j]/3.0)
        if (value>=P): count+=1
        elif(value+1>=P and S>0):
            count+=1
            S-=1

    print "Case #%d: %d" %(i+1,count)
