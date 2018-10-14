#!/usr/bin/env python

def solve(case_nr):
  [D, N] = map(int, raw_input().split())
  
  arrival_time = 0
  
  for i in xrange(N):
    [K, S] = map(int, raw_input().split())
    time = (D-K)/float(S);
    arrival_time = max(arrival_time, time)
  
  print "Case #%d: %.6f" % (case_nr, (D/arrival_time))


T = int(raw_input())

for i in xrange(T):
  solve(i+1)
