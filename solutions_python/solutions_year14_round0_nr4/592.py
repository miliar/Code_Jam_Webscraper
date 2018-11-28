#!/usr/bin/env python
import sys
import copy
from collections import deque

def solve():
  blocks = int(sys.stdin.readline())
  for i in xrange(blocks):
    naomi1 = deque(sorted(map(float, sys.stdin.readline().split()), reverse = True))
    ken1 = deque(sorted(map(float, sys.stdin.readline().split()), reverse = True))
    naomi2 = copy.copy(naomi1)
    ken2 = copy.copy(ken1)

    def removeMinWinner():
      n = ken1[-1]
      lst = []
      while naomi1[-1] < n:
        lst.append(naomi1.pop())
      naomi1.pop()
      naomi1.extend(lst)

    lie, truth = 0, 0
    while len(naomi1) > 0:

      if naomi1[0] > ken1[0]:
        lie += 1
        removeMinWinner()
        ken1.pop()
      else:
        naomi1.pop()
        ken1.popleft()

      # naomi plays her best, ken reacts
      if naomi2[0] > ken2[0]:
        truth += 1
        naomi2.popleft()
        ken2.pop()
      else:
        naomi2.popleft()
        ken2.popleft()

    return lie, truth

tests = int(sys.stdin.readline())
for case in xrange(1, tests + 1):
  lie, truth = solve()
  print "Case #%d: %d %d" % (case, lie, truth)
