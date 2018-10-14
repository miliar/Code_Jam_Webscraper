#!/usr/bin/python

import sys

def recycledpartners(n,B):
  sn = str(n)
  l = len(sn)
  sn2=sn+sn
  S = []
  for i in range(1,l):
    if (sn2[i]!='0'):
      sm = sn2[i:i+l]
      m = int(sm)
      if (n<m and m<=B and m not in S):
        S.append(m)
  return len(S)

T = int(sys.stdin.readline())
for i in range(T):
  tok = sys.stdin.readline().strip().split()
  A = int(tok[0])
  B = int(tok[1])
  C = 0

  #print A,B
  for n in range(A,B):
    C += recycledpartners(n,B)

  print "Case #%d: %d" % (i+1,C)

