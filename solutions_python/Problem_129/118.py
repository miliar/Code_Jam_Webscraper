#!/usr/bin/python

import sys

def cost_for_trip(N,dist):
  if dist <= 0:
    return 0
  else:
    return dist*N - dist*(dist-1)/2

T = int(sys.stdin.readline())
for test in range(T):
  # print >> sys.stderr, "Test: %d" % (test+1)
  toks = sys.stdin.readline().strip().split()
  N = int(toks[0])
  M = int(toks[1])
  # print N,M

  trips = []
  for i in range(M):
    toks = sys.stdin.readline().strip().split()
    o = int(toks[0])
    e = int(toks[1])
    p = int(toks[2])
    trips.append([o,e,p])
  # print trips

  expected = 0
  for t in trips:
    d = t[1] - t[0]
    if d > 0:
      expected += cost_for_trip(N,d) * t[2]
  # print expected

  actual = 0
  tickets = []
  for i in range(1,N+1):
    for t in trips:
      if i == t[0]:
        tickets += t[2]*[i]
    for t in trips:
      if i == t[1]:
        tickets.sort()
        for j in range(t[2]):
          tt = tickets.pop()
          d = i - tt
          cost = cost_for_trip(N,d)
          # print tt,i,d,cost
          actual += cost
  # print actual

  if expected < actual:
    print >> sys.stderr, "Error!!!"
  loss = expected - actual

  print "Case #%d: %d" % (test+1,loss%1000002013)

