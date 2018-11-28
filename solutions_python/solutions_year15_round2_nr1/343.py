# coding: utf-8

import sys

T = int(sys.stdin.readline())

for t in xrange(1, T + 1):
  N = int(sys.stdin.readline())
  cnt = 1
  while N > 1:
    if N < 20:
      cnt += N - 1
      break
    l = len(str(N))
    m = 10 ** ((l + 1) / 2)
    if N % m == 0:
      N -= 1
      cnt += 1
    else:
      d = N / m
      if int(str(d)[::-1]) == 1:
        N -= 1
        cnt += 1
      else:
        k = d * m + 1
        cnt += N - k + 1
        N = int(str(k)[::-1])
  print "Case #%d: %d" % (t, cnt)
