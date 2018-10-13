#!/usr/bin/env python
# (c) Christoph Grenz

from sys import stdin, stdout, stderr
from copy import copy

count = int(stdin.readline().strip())

GOAL = 'welcome to code jam'

def countOccurences(haystack, needle=GOAL):
  maxlevel = len(needle)-1
  maxbegin = len(haystack)-len(needle)
  if maxbegin < 0:
    return 0

  def rek(start=0,level=0):
    if level == maxlevel+1:
      return 1

    r = 0
    for i in xrange(start,len(haystack)):
      if i > maxbegin+level:
        break

      c = haystack[i]
      if c == needle[level]:
        r += rek(i+1,level+1)
    return r
  return rek()

for x in xrange(count):
  line = stdin.readline().strip()
  print 'Case #%i:' % (x+1),
  print str(countOccurences(line))[-4:].zfill(4)
