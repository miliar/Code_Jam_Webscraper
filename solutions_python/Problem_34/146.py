#!/usr/bin/env python
import re
L,D,N = map(int, raw_input().split())
words = ";".join([raw_input() for i in xrange(D)])
posible = [raw_input().replace("(","[").replace(")","]") for i in xrange(N)]
for i in xrange(len(posible)):
   K = len(re.findall(posible[i],words))
   print "Case #%d: %d" % (i+1,K)

