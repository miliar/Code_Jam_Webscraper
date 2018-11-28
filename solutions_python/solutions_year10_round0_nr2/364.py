#!/usr/bin/python

import os
import sys

fn = sys.argv[1]

fh = open(fn, "r")
C = int(fh.readline().strip())
cases = []
for i in range(C):
  cases += [map(long, fh.readline().strip().split(" "))]

try:
  cases += [map(long, fh.readline().strip().split(" "))]
except:
  print "good read"

fh.close()

#http://mail.python.org/pipermail/edu-sig/2000-September/000610.html
def gcd(a,b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
       a, b = b, a % b
    return a



fh = open("outb.txt","w")
for (i,case) in enumerate(cases):
  times = case[1:]
  if len(times) != case[0]:
    print i
  min_time = min(times)
  times0 = map(lambda x: x-min_time, times)
  gcd1 = gcd(times0[0],times0[1])
  if len(times) > 2:
    for time in times0[2:]:
      gcd1 = gcd(gcd1,time)
  #print gcd1
  time_past = min_time % gcd1
  if time_past != 0:
    print >> fh, "Case #"+str(i+1)+": "+str(gcd1-time_past)
  else:
    print >> fh, "Case #"+str(i+1)+": 0"

fh.close()
