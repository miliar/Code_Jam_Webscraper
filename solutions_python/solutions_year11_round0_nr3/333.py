#!/usr/bin/python
import sys

TC=0
DEBUG=False
if len(sys.argv)>2:
  DEBUG=True
  TC=int(sys.argv[2])

def debugprint(s,t):
  if DEBUG and(t==TC):
      print s

input = open (sys.argv[1],'r')
T = int(input.readline())
for t in range(0,T):
  S = 0
  N = int(input.readline())
  X = map(int,input.readline().rstrip().split(' '))
  X.sort()
  SS = 0;
  for x in X:
    SS = SS ^ x
    S = S + x
  debugprint((SS,S,X),t)
  if SS != 0:
    S = "NO"
  else:
    S = S - X[0]
  print "Case #%d:" % (t+1),S

