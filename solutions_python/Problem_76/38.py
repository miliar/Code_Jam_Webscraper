#!/usr/bin/python

import os
import sys

fn = sys.argv[1]

fh = open(fn, "r")
T = int(fh.readline().strip())
cases = []
for i in range(T):
  fields = fh.readline().strip().split()
  N = int(fields[0])
  fields = fh.readline().strip().split()
  n_s = map(lambda x: int(x), fields)
  if len(n_s)!=N:
    print "read error"
  cases += [n_s]

#print cases

try:
  line = fh.readline().strip()
  if line == "":
    print "good read"
except:
  print "good read"

fh.close()


#http://www.daniweb.com/code/snippet216539.html#

def int2bin(n, count=24):
    """returns the binary of integer n, using count number of digits"""
    return "".join([str((n >> y) & 1) for y in range(count-1, -1, -1)])


fh = open("out.txt","w")
for (i,case) in enumerate(cases):
  n_s = case
  b_s = []
  for n in n_s:
    b_s += [int2bin(n)]
  problem = 0
  for loc in range(len(b_s[0])):
    if sum(map(lambda x: int(x[loc]), b_s))%2==1:
      problem = 1
      break
  if problem == 1:
    print >> fh, "Case #"+str(i+1)+": NO"
  else:
    print >> fh, "Case #"+str(i+1)+": "+str(sum(n_s)-min(n_s))

fh.close()

