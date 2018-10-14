#!/bin/python

filename = "A-large"

infile = open("%s.in" % filename,"rb")
outfile = open("%s.out" % filename, "wb")

T = int(infile.readline())
for i in xrange(T):
    N, K = map(int, infile.readline().split())
    mask = (1 << N) - 1
    outfile.write("Case #%d: %s\n" % (i+1, "ON" if (mask & K) == mask else "OFF"))

infile.close()
outfile.close()