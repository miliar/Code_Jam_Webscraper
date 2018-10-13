#!/bin/python
from math import log, ceil

filename = "B-large"

infile = open("%s.in" % filename,"rb")
outfile = open("%s.out" % filename, "wb")

T = int(infile.readline())
for case in xrange(T):
    L, P, C = map(int, infile.readline().split())
    
    a = L
    K = 0
    if a * C < P:
        K = ceil(log(log(float(P)/L,C),2.))
    
    outfile.write("Case #%d: %d\n" % (case+1, K))

infile.close()
outfile.close()