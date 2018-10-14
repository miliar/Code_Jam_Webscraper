# coding: utf-8

import sys

T = int(sys.stdin.readline())
memo = {}

def do(v):
  if v in memo:
    return memo[v]
  for i in xrange(len(v) - 1, 0, -1):
    if v[i] > 0:
      break
  if i == 1:
    memo[v] = 1
  else:
    b = do(tuple(list(v)[1:] + [0]))
    for x in xrange(1, i / 2 + 1):
      y = i - x
      w = list(v)
      w[x] += 1
      w[y] += 1
      w[i] -= 1
      a = do(tuple(w))
      if a < b:
        b = a
    memo[v] = b + 1
  return memo[v]

for t in xrange(1, T + 1):
  D = int(sys.stdin.readline())
  w = [0,] * 10
  for p in sys.stdin.readline().split():
    p = int(p)
    w[p] += 1
  print "Case #%d: %d" % (t, do(tuple(w)))
