#!/usr/bin/python

import sys

def topnonsurprise(t):
  td3 = t/3
  tm3 = t%3

  tn = td3
  if (tm3>=1):
    tn+=1

  ts = td3
  if (tm3>0):
    ts+=tm3
  elif (td3>0):
    ts+=1

  return (tn,ts)

T = int(sys.stdin.readline())
for i in range(T):
  tok = sys.stdin.readline().strip().split()
  N = int(tok[0])
  S = int(tok[1])
  p = int(tok[2])

  t = [0] * N
  for j in range(N):
    t[j] = int(tok[j+3])

  #print N, S, p, t

  B=0
  s=S
  for j in range(N):
    (tn,ts)=topnonsurprise(t[j])
    #print t[j],tn,ts
    if (tn>=p):
      B+=1
    elif (ts>=p and s>0):
      B+=1
      s-=1

  print "Case #%d: %d" % (i+1,B)

