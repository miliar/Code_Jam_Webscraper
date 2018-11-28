#! /usr/bin/env python

import sys

N = int(sys.stdin.readline())

for n in range(1, N+1):
  l=sys.stdin.readline().split(" ");
  N=int(l[0])
  K=int(l[1])
  on =  (K & ((1<<N)-1))+1 == 1<<N 
  print 'Case #%d: %s' % (n, "ON" if on else "OFF")

