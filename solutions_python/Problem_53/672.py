# -*- coding:utf-8 -*-

import sys,os

def ReadInt():
  line = sys.stdin.readline().rstrip("\n").split()
  return map(int,line)

def IsLight(n,k):
  if k == 0:
    return False
  elif k == ((2**N) - 1):
    return True
  else:
    return False

T = ReadInt()[0]
for i in xrange(1,T+1):
  N,K = ReadInt()
  # if N == 1:
  #   if K % 2 == 0: ret = False
  #   else: ret = True
  # else:
  K = K % (2**N)
  ret = IsLight(N,K)
  if ret:
    print "Case #%d: ON"%i
  else:
    print "Case #%d: OFF"%i


