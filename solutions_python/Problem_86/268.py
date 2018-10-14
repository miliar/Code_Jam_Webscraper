#!/usr/bin/python
import sys
from solve import *

f = open(sys.argv[1], "r")

lines = f.readlines()[1:] # skip first line

c = 1
i = 0
while i < len(lines):
  n, l, h = map(int,lines[i].split(" "))
  numbers = map(int,lines[i+1].split(" "))
  s = solve(l, h, numbers)

  if s == None:
    print "Case #%s: %s" % (c, "NO")
  else:
    print "Case #%s: %s" % (c, s)

  i += 2
  c += 1
