#!/usr/bin/env python
import sys

def solve(N,K):
    rnd = 2**N
    return (K % rnd == (rnd-1))

##############################################

for i,line in enumerate(file(sys.argv[1])):
    line = line.strip()
    if i==0:
        N=int(line)
        continue

    N,K = map(int,line.split())
    res = solve(N,K)
    if res:
        print "Case #%d: ON" % i
    else:
        print "Case #%d: OFF" % i

##############################################

