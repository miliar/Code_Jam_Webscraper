#! /usr/bin/python

import sys

def solve(n, wire):
  crossing = 0

  for i in xrange(n):
    for j in xrange(i+1, n):
      if wire[j][1] < wire[i][1]:
        crossing += 1

  return crossing

fd = open(sys.argv[1])
num_cases = int(fd.readline())

for j in range(0, num_cases):
  n = int(fd.readline())
  wire = []
  for i in xrange(n):
    wire.append([int(item) for item in fd.readline().split(" ")])

  wire = sorted(wire, key=lambda w: w[0])

  output = solve(n, wire)
  print "Case #%d:" % (j+1), output

