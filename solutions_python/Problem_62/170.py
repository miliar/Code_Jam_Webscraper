#!/usr/bin/env python

cases = int(raw_input())
for case in range(cases):
  num_wires = int(raw_input())
  wires = []
  intersections = 0

  for i in range(num_wires):
    wires.append(map(int, raw_input().split()))

  for (i, a) in enumerate(wires):
    for (j, b) in enumerate(wires[i + 1:]):
      if a[0] > b[0] and a[1] < b[1] or a[0] < b[0] and a[1] > b[1]:
        intersections += 1

  print "Case #%d: %d" % (case + 1, intersections)
