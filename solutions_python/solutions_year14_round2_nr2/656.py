#!/usr/bin/env python

T = int(raw_input())

for x in range(1, T+1):
  A, B, K = map(int, raw_input().split())
  possible = set([])
  counter = 0
  for i in range(A):
    for j in range(B):
      possible.add((i,j))
  for winner in possible:
    if winner[0] & winner[1] < K:
      counter = counter + 1
  print "Case #"+str(x)+": "+str(counter)


