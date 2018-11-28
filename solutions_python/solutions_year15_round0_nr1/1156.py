#!/usr/bin/env python
import os,sys,string
fp = open("A-large.in", "rt")
T = int(fp.readline())
for trial in range(0, int(T)):
  data = fp.readline().strip().split()
  
  Smax = int(data[0])
  members = data[1]

  acc, need = 0, 0
  for ind, digit in enumerate(members):
    num = int(digit)
    if acc + need < ind:
      need += (ind - (acc + need))
    acc += num

  print "Case #%d: %d" % (trial + 1, need)
