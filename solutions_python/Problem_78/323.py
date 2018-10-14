#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
from fractions import gcd

def solve(N,PD,PG):
  if PD != 100 and PG == 100:
    return False
  if PD != 0 and PG == 0:
    return False
  Dmin = 100/gcd(100,PD)
  Wd = PD/gcd(100,PD)
  if Dmin <= N and PD > PG:
    return True
  m = 1
  while( m*Dmin <= N ):
    num = PG - m*Wd
    den = 100 - m*Dmin
    if num*den >= 0 and (abs(num) <= abs(den)):
      return True
      break
    m += 1
  return False
  
T = int(sys.stdin.readline().rstrip("\n"))
for prob in xrange(1,T+1):
  N,PD,PG = map(int,sys.stdin.readline().rstrip("\n").split())
  b = solve(N,PD,PG)
  if b:
    s = "Possible"
  else:
    s = "Broken"
  print "Case #%d: %s"%(prob,s)
  
