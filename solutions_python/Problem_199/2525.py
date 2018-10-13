#!/usr/bin/env python

t = int(raw_input())
for i in xrange(1, t + 1):
  nflips = 0
  s, k = raw_input().split(" ")
  s = map(lambda c: c == '+', s)
  k = int(k)
  for j in xrange(0, len(s) - k + 1):
    if not s[j]:
      # flip pancakes
      for f in xrange(j, j + k):
        s[f] = not s[f]
      nflips += 1
  possible = all(c for c in s)
  answer = nflips if possible else "IMPOSSIBLE"
  print "Case #{}: {}".format(i, answer)
