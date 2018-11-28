#!/usr/bin/env python

T = int(raw_input())

for x in range(1, T+1):
  info = map(float, raw_input().split())
  C = info[0]
  F = info[1]
  X = info[2]
  farm = 2
  t = 0
  while(farm < (X-C)*F/C):
    t = t + C/farm
    farm = farm + F
  t = t + X/farm
  print "Case #"+str(x)+": "+'{0:.8f}'.format(round(t,7))

