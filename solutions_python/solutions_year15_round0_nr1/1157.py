#!/usr/local/bin/python

import sys
import math

T = int(sys.stdin.readline())

for caseno in xrange(T):
   mshy, shyness = sys.stdin.readline().strip().split()

   added = 0
   standing = 0

   for i, count in enumerate(shyness):
       count = int(count)
       if standing >= i:
           standing += count
       else :
           extra = (i - standing)
           added += extra
           standing += count + extra

   ans = added
   print "Case #%d: %d" % (caseno + 1, ans)


