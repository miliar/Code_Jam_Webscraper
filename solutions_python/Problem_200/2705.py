#!/usr/bin/env python

t = int(raw_input())
for i in xrange(1, t + 1):
  n = list(raw_input())
  # number of 9s to fill at the end
  fill_nines = 0
  for j in xrange(len(n) - 1):
    if n[len(n) - j - 2] > n[len(n) - j - 1]:
      n[len(n) - j - 2] = chr(ord(n[len(n) - j - 2]) - 1)
      fill_nines = j + 1
  # fill nines
  for j in xrange(fill_nines):
    n[len(n) - 1 - j] = '9'
  # strip leading zeros
  solution = ''.join(n).lstrip('0')
  print "Case #{}: {}".format(i, solution)
