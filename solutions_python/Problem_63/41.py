from collections import deque
from math import *

import sys
inp = sys.stdin

T = int(inp.readline())
for cas in xrange(1, T+1):
  print "Case #%d:" % (cas),
  L, P, C = (int(x) for x in inp.readline().split(' '))
  count = 1
  l = L*C
  while l < P:
    count += 1
    l *= C
  print int(ceil(log(count, 2)))
  