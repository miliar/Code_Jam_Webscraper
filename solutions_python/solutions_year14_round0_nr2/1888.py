#!/usr/bin/python
import sys
T = int(sys.stdin.readline())
for case in range(1,T+1):
  C,F,GOAL=map(float,sys.stdin.readline().strip().split())
  time = 0.0
  rate = 2.0
  investment_return_time = C / F
  if F>0.0:
   while GOAL/rate > (GOAL/(rate+F) + C/rate):
    time += C/rate
    rate += F
  time += GOAL/rate
  print "Case #%i: %.7f" % (case,time)
