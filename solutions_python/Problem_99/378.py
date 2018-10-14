#!/usr/bin/env python
import sys

stin = sys.stdin
stin.readline()

lines = stin.readlines()

for i in range(len(lines)/2):
    (a,b) = map(int, lines[2*i].split())
    px = map(float, lines[2*i+1].split())
    px.append(0.0)

    expt = (a+1) * [0]
    for j in range(a+1): # mistake in jth
        p = reduce(lambda x,y: x*y, px[:j],1) * (1.0 - px[j])
        for k in range(a+1): # type bs k times
            if j >= (a-k):
                expt[k] += p * (b-a + 2*k + 1)
            else:
                expt[k] += p * (b-a + 2*k + 1 + b + 1)
    
    expt.append(float(b+2))
    print "Case #%d: %.6f" % ((i+1), apply(min, expt))
