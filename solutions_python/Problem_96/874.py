#!/usr/bin/env python

def best_triple_part(n):
  if n == 0:
    return 0
  elif n < 3:
    return 1
  else:
    if score%3 == 0:
      return score//3
    return score//3+1

def best_surprise_part(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  elif n==2:
    return 2
  else:
    if score%3 == 2:
      return score//3+2
    return score//3+1

import sys

T = int(sys.stdin.readline())

for t in range(1,T+1):
  ns = [int(n) for n in sys.stdin.readline().split()]
  N,S,p = ns[:3]
  scores = ns[3:]
  count = 0
  for score in scores:
    if best_triple_part(score) >= p:
      count+=1
    elif S > 0 and best_surprise_part(score) >= p:
      S -= 1
      count += 1
  print('Case #%s: %s' % (t, count))

