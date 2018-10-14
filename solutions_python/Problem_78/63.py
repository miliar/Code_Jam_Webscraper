#!/usr/bin/python

import os
import sys
import math
import fractions

fn = sys.argv[1]

fh = open(fn, "r")
T = int(fh.readline().strip())
cases = []
for i in range(T):
  fields = fh.readline().strip().split()
  cases += [map(int, fields)]

#print cases

try:
  line = fh.readline().strip()
  if line == "":
    print "good read"
except:
  print "good read"

fh.close()


fh = open("out.txt","w")
for (i,case) in enumerate(cases):
  [n,d,g] = case
  gcd_d = fractions.gcd(100,d)
  min_won = d/gcd_d
  min_played = 100/gcd_d
  #print case, min_won, min_played
  if n < min_played:
    print >> fh, "Case #"+str(i+1)+": Broken"
  else:
    if g < 100 and g > 0:
      print >> fh, "Case #"+str(i+1)+": Possible"
    else:
      if g == 100 and d == 100:
        print >> fh, "Case #"+str(i+1)+": Possible"
      elif g == 100 and d != 100:
        print >> fh, "Case #"+str(i+1)+": Broken"
      elif g == 0 and d != 0:
        print >> fh, "Case #"+str(i+1)+": Broken"
      elif g == 0 and d == 0:
        print >> fh, "Case #"+str(i+1)+": Possible"
      else:
        print "problem", case

fh.close()

