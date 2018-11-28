#!/usr/bin/python

import sys

f = open(sys.argv[1],'r')
t = int(f.readline())

for case in xrange(t):
  abk = [int(x) for x in f.readline().split()]
  total_count = 0
  #for every value of k count number of ways to create
  for a in xrange(abk[0]):
    for b in xrange(abk[1]):
      if a&b < abk[2]:
        total_count += 1
  print "Case #" + str(case+1) + ":", total_count
