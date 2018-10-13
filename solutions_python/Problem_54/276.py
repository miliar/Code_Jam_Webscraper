#! /usr/bin/env python

import sys
import fractions

C = int(sys.stdin.readline())

for c in range(1,C+1):
  list = map(int, sys.stdin.readline().split(" "))
  N = list[0]
  list = list[1:len(list)]
  gcd1 = reduce(fractions.gcd, list)
  slist = map(lambda x: x/gcd1, list)
  for i in range(0,len(list)):
    list[i] = abs(slist[i] - slist[(i+1)%len(list)])
  gcd2 = reduce(fractions.gcd, list)
  if gcd2 == 1:
    print "Case #%d: %d" % (c, 0)
  else:
    print "Case #%d: %d" % (c, ((slist[0]/gcd2+1)*gcd2 - slist[0])*gcd1)

