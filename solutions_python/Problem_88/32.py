from __future__ import division
from math import sqrt

f = [l[:-1] for l in file("in")][1:]

case = 0
while len(f):
  case += 1

  height, width, expected = [int(x) for x in f.pop(0).split(" ")]
  arr = []
  for h in xrange(height):
    arr.append([expected + int(x) for x in f.pop(0)])

  best = 0
  for x1 in xrange(height):
    for x2 in xrange(x1 + 1, height):
      for y1 in xrange(width):
        thiswidth = (x2 - x1) + 1
        y2 = y1 + (x2 - x1)
        if y2 >= width or thiswidth < 3: continue
        centerx = (x2 + x1) / 2
        centery = (y2 + y1) / 2
        calccenterx = 0
        calccentery = 0

        for x in range(x1, x2+1):
          for y in range(y1, y2+1):
            if (x == x1 and y == y1) or (x == x1 and y == y2) or (x == x2 and y == y1) or (x == x2 and y == y2): continue
            calccenterx += (x - centerx) * arr[x][y]
            calccentery += (y - centery) * arr[x][y]

        if calccenterx == 0 and calccentery == 0:
          if thiswidth > best:
            best = thiswidth


  if best == 0:
    print "Case #%d: %s" % (case, "IMPOSSIBLE")
  else:
    print "Case #%d: %d" % (case, best)

