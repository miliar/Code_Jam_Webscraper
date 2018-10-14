#!/usr/bin/env python
import sys

def ReadFile(fname):
  f = open(fname,'r')
  for word in f.read().split():
    yield word

fin = ReadFile(sys.argv[1])
T   = int(next(fin))
for t in range(T):
  # print "----------------"
  smax         = int(next(fin))
  shy          = next(fin)
  shy          = map(int,list(shy))
  standing     = 0
  extra_needed = 0
  for idx,num in enumerate(shy):
    # print idx,num
    if num and standing<idx:
      # print "Adding %d. Have: %d" % (idx-standing, standing)
      extra_needed += idx-standing
      standing     += idx-standing+num
    else:
      standing += num
      # print "Have %d" % (standing)
  print "Case #%d: %d" % (t+1,extra_needed)