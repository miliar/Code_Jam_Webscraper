#!/usr/bin/env python
from collections import deque

T = int(raw_input())
for case in range(T):
  R, k, N = [int(s) for s in raw_input().split(' ')]
  g = deque([int(s) for s in raw_input().split(' ')])
  money = 0
  for run in range(R):
    people = 0
    i = 0
    finished = False
    while not finished:
      if i == N: break
      i += 1
      next_g = g.popleft()
      if people + next_g > k:
        finished = True
        g.appendleft(next_g)
      else:
        people += next_g
        g.append(next_g)
    money += people
  print 'Case #%i: %i' % (case+1, money)
