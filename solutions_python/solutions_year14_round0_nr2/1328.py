#!/usr/bin/python
import os,sys
T=int(raw_input())
for t in range(T):
  [C, F, X] = ([float(e) for e in raw_input().split()])
  R = 2
  res = X/R
  time = 0.0
  while res >= time:
    #check next farm   
    time += C/R
    R += F
    res = min(res, X/R+time)
  print 'Case #'+str(t+1)+': '+str(res)

