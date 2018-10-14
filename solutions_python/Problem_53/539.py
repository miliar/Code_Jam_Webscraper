#!/usr/bin/env python
import sys

file = open(sys.argv[1])
for i in xrange(1,int(file.readline())+1):
    n,k = [int(x) for x in file.readline().strip().split()]
    print "Case #%d: %s" % (i,"ON" if k & (2**n-1) == (2**n-1) else "OFF")
