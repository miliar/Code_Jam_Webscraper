from collections import deque

import sys
inp = sys.stdin

T = int(inp.readline())
for cas in xrange(1, T+1):
  print "Case #%d:" % (cas),
  N = int(inp.readline())
  As = []
  Bs = []
  for i in xrange(N):
    a, b = (float(x) for x in inp.readline().split(' '))
    As.append(a)
    Bs.append(b)
  inter = 0
  for i in xrange(N):
    for j in xrange(i+1, N):
      x = (As[j] - As[i])
      y = (Bs[i]-As[i]-Bs[j]+As[j])
      if y != 0 and 0 < x/y < 1:
        inter += 1
  print inter