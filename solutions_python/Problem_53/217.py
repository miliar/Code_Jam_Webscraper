#!/usr/bin/env python

T = int(raw_input())
for case in range(T):
  N, K = [int(i) for i in raw_input().split(' ')]
  if (K+1) % 2**N == 0:
    s = 'ON'
  else:
    s = 'OFF'
  print 'Case #%i: %s' % (case+1, s)  
