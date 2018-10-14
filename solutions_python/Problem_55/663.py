# -*- coding:utf-8 -*-
import sys,os

def ReadInt():
  line = sys.stdin.readline().rstrip("\n").split()
  return map(int,line)

def grouptogo(k,gq):
  s = 0
  ride = []
  while gq:
    if s + gq[0] <= k:
      s += gq[0]
      ride.append(gq.pop(0))
    else:
      break
  gq += ride
  return s

T = ReadInt()[0]
for prob in xrange(1,T+1):
  R,K,N = ReadInt()
  gq = ReadInt()
  s = 0
  for i in xrange(R):
    s += grouptogo(K,gq)
  print "Case #%d: %d"%(prob,s)


