#!/usr/bin/python
import sys

input = open (sys.argv[1],'r')
T = int(input.readline())
for t in range(0,T):
  X = map(int,input.readline().rstrip().split(' '))
  X.sort()
  R=0
  for x in range(X[0],X[1]):
    S=str(x)
    prev=""
    for i in range(0,len(S)):
      S2=S[i:]+S[0:i]
      if (X[1]>=int(S2)>x) and prev!=S2:
        R+=1
        prev=S2
  print "Case #%d:" % (t+1),R

