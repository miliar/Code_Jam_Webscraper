#!/usr/bin/python
import sys
T = int(sys.stdin.readline())
for t in range(T):
  N = int(sys.stdin.readline())
  v = map(int, sys.stdin.readline().split())
  xor = 0
  sum = 0
  pat = 1000000
  for n in range(N):
    xor ^= v[n]
    sum += v[n]
    if (v[n] < pat):
      pat = v[n]
  if xor == 0:
    print "Case #%d: %d" % (t+1, sum - pat)
  else:
    print "Case #%d: NO" % (t+1)
