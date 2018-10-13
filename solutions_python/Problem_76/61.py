#!/usr/bin/env python

import sys
import math

bin = [1,2,4,8,
       16,32,64,
       128,256,512,
       1024,2048,4096,8192,
       16384,32768,65536,
       131072]
C = int(sys.stdin.readline())
for xxx in xrange(C):
    sys.stdin.readline()
    l = [int(x) for x in sys.stdin.readline().split()]
    tot = reduce(lambda x,y: x ^ y, l)
    if tot != 0:
        print "Case #" + str(xxx+1) + ": NO"
    else:
        print "Case #" + str(xxx+1) + ": %d" % (sum(l) - min(l))





