#!/usr/bin/env python

import sys

f=sys.stdin
n=int(f.next())


for case in range(1, n+1):
    l = f.next()
    x = sorted(map(int,f.next().split()))
    y = sorted(map(int,f.next().split()), reverse=True)
    print "Case #%s: %s"%(case,sum(d[0]*d[1] for d in zip(x,y)))


