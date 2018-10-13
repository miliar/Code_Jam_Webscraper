#!/usr/bin/env python
import sys

def readline(): return sys.stdin.readline().strip()
def readrow(): return readline().split(' ')
def xor(x, y): return x^y
def sumgf2(l): return 0 if len(l) == 0 else reduce(xor, l)

T = int(readline())
for t in range(T):
  c = int(readline())
  candies = map(int, readrow())
  # check if we can separate candies without Patrik crying
  if reduce(xor, candies) != 0:
    print 'Case #%d: NO' % (t+1)
    continue

  candies.sort()
  res = sum(candies[1:])
  print 'Case #%d: %d' % (t+1, res)

