#! /usr/bin/python

import psyco
psyco.full()

fd = open("input.in")

num_cases = int(fd.readline())

def solve(n, m, a):
  for xb in range(0, n+1):
    for xc in range(1, n+1):
      for yc in range(1, m+1):
        (yb, rem) = divmod(xb * yc - a, xc)
        if rem == 0 and yb >= 0 and yb < (m+1):
          area = abs(xb*yc - xc*yb)
          if a == area:
            return "0 0 %d %d %d %d" % (xb, yb, xc, yc)
        (yb, rem) = divmod(a - xb * yc, xc)
        if rem == 0 and yb >= 0 and yb < (m+1):
          area = abs(xb*yc - xc*yb)
          if a == area:
            return "0 0 %d %d %d %d" % (xb, yb, xc, yc)
  return "IMPOSSIBLE"

for i in range(0, num_cases):
  (n, m, a) = [int(item) for item in fd.readline().split(" ")]
  output = solve(n, m, a)
  print "Case #%d:" % (i+1), output
