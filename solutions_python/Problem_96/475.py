#!/usr/bin/env python
import sys
row = 0
for line in sys.stdin:
  row += 1
  if row == 1:
    continue
  xs = [ int(x) for x in line.split(" ") ]
  n,s,p = xs[:3]
  ts = xs[3:]
  count = 0
  for t in reversed(sorted(ts)):
    if t >= 3*p - 2:
      count += 1
    elif s > 0 and t >= 2 and t >= 3*p - 4:
      s -= 1
      count += 1
    else:
      break
  print "Case #%d: %d"%(row-1,count)
