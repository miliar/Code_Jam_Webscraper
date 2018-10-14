#!/usr/bin/env python
import sys

# Open
fname = sys.argv[1]
f = open(fname,'r')
g = open(fname + '.out','w')

# Functions

# Do
T = int(f.readline())
for i in range(T):
  line = f.readline().split()
  Smax, Slist = int(line[0]), line[1]
  Sk = 1
  up = int(Slist[0])
  friends = 0
  while Sk <= Smax:
    if up >= Sk:
      up += int(Slist[Sk])
      Sk += 1
    else:
      supl = Sk - up
      friends += supl
      up += int(Slist[Sk]) + supl
      Sk += 1

  # Out
  x = i + 1
  y = friends
  s = 'Case #' + str(x) + ': ' + str(y)
  g.write(s + '\n')

# Close
f.close()
g.close()
