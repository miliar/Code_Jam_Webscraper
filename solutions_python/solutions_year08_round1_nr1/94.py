#!/usr/bin/python

import sys
import math
from collections import deque

try:
  import psyco
  psyco.full()
except Exception, e:
  pass

def solve(S1, S2):
  S1 = deque(S1)
  S2 = deque(S2)

  T = 0
  while len(S1):
    A = S1[0] * S2[-1]
    B = S1[-1] * S2[0]
    if A <= B:
      S1.popleft()
      S2.pop()
      T += A
    else:
      S2.popleft()
      S1.pop()
      T += B

  return T

if __name__ == '__main__':
  if len(sys.argv) != 2:
     print ('Usage: %s file' % sys.argv[0])
     sys.exit(1)

  f = open(sys.argv[1])
  NTEST =  int(f.readline())

  for i in xrange(NTEST):
    print ('Case #%d:' % (i + 1)),
    dummy =  int(f.readline())
    S1 =  sorted(map(int, f.readline().split()))
    S2 =  sorted(map(int, f.readline().split()))
    print solve(S1, S2)
