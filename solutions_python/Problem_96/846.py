#!/usr/bin/python
import math
import sys

input = open (sys.argv[1],'r')
T = int(input.readline())
for t in range(0,T):
  X = map(int,input.readline().rstrip().split(' '))
  S = X[1]
  p = X[2]
  R = 0
  Y = X[3:]
  Y.sort()
  Y.reverse()
  p1=p-1 if (p-1>0) else 0
  p2=p-2 if (p-2>0) else 0
  for i in range(0,X[0]):
    if Y[i]>=p+(p1)*2:
      R=R+1
    elif Y[i]>=p+(p2)*2 and S>0:
      R=R+1
      S=S-1
    else:
      break
  print "Case #%d: %d" % (t+1,R)

