#!/usr/bin/env python

import math

def solve(case_nr):
  [N, K] = map(int, raw_input().split())
  
  l=[]
  for i in xrange(N):
    [r,h] = map(int, raw_input().split())
    l.append((r,h))
  
  #print l

  best_area = 0
  for i in xrange(N):
    base = l[i]
    remainder = [2*r*h for (r,h) in l if r <=  base[0]]
    remainder.remove(2*base[0]*base[1])
    remainder.sort(reverse=True)
    #print base
    #print remainder
    if len(remainder) >= (K-1):
      area = base[0]*base[0] + 2 * base[0] * base[1]
      area += sum(remainder[:(K-1)])
      
      #if (area>best_area):
      #  print base, sorted(remainder[:(K-1)], reverse=True)
      best_area = max(best_area, area)  

  print "Case #%d: %.9f" % (case_nr, best_area * math.pi)


T = int(raw_input())

for i in xrange(T):
  solve(i+1)
