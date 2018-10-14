#!/usr/bin/python

import re

rl = raw_input

l,d,n = map(int,rl().split())
words = []
for i in xrange(d):
  words.append(rl())
for x in xrange(1,n+1):
  pat = re.compile(rl().replace("(","[").replace(")","]") + "$")
  cnt = 0
  for word in words:
    if pat.match(word):
      cnt += 1
  print "Case #%d: %d" % (x,cnt)

