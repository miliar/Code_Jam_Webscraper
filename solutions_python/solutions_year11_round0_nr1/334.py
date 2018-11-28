#!/usr/bin/python
import math
import sys

input = open (sys.argv[1],'r')
T = int(input.readline())
for t in range(0,T):
  STATE =dict({'O': [ 1, 0 ], 'B': [ 1, 0 ]})
  S = 0
  X = input.readline().rstrip().split(' ')
  for i in range(0,int(X[0])):
    B= X[1+i*2]
    P= int(X[2+i*2])
    q = S - STATE[B][1]
    d = math.fabs(P - STATE[B][0])
    S = S + max(d-q,0) +1
    STATE[B][0]=P
    STATE[B][1]=S
    #print S,B,P,q,d,STATE
  #print n,X,Y,S
  print "Case #%d: %d" % (t+1,S)

