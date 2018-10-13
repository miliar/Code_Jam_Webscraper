#!/usr/bin/env python

import sys


def ok(lines,y,x):
  # check if grass is within 1-100 mm
  height=lines[y][x]
  if lines[y][x] <=0 or lines[y][x] > 100:
    return False
  # check if horizontal row is okay
  hok = True
  for i in range(m):
    if lines[y][i] > height:
      hok=False
      break
  # check if vertical row is okay
  vok = True
  for i in range(n):
    if lines[i][x] > height:
      vok=False
      break

  return hok or vok


with open(sys.argv[1],'r') as f:
  t = int(f.readline())
  for z in range(t):
    n,m = map(int,f.readline().split())
    lines = []
    for nn in range(n):
      lines.append(map(int,f.readline().split()))

    fail = False
    for y in range(n):
      for x in range(m):
        if not ok(lines,y,x):
          fail=True
          break
      if fail:
        break
    if fail:
      print "Case #%d: NO"%(z+1)
    else:
      print "Case #%d: YES"%(z+1)

