#!/usr/bin/python2
#-*- coding: utf-8 -*-

import heapq

def readint(): return int(raw_input())
def readarray(f): return map(f, raw_input().split())

def cost(N, o, e):
  k = e - o
  return k*N - k*(k-1)/2

for test in range(readint()):
  print 'Case #%i:'%(test+1),
  N, M = readarray(int)
  
  events = []
  normal_cost = 0
  for i in range(M):
    o, e, p = readarray(int)
    events.append((o, 0, p))
    events.append((e, 1, p))
    normal_cost += p * cost(N, o, e)
  
  events.sort()
  available = []

  real_cost = 0

  for event in events:
    p = event[2]
    if event[1] == 0:
      o = event[0]
      heapq.heappush(available, (-o, p))
    else:
      e = event[0]
      while p > 0:
        mo, q = heapq.heappop(available)
        o = -mo
        if q > p:
          heapq.heappush(available, (mo, q-p))
          real_cost += p * cost(N, o, e)
          p = 0
        else:
          real_cost += q * cost(N, o, e)
          p -= q

  print normal_cost - real_cost
