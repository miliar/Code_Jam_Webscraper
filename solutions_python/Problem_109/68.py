import math
import random

infile = open("B-small.in", "r")
outfile = open("B-small.out", "w")

data = [l.strip() for l in infile.readlines()]

def intersect(r1, x1, y1, r2, x2, y2):
  dbetween = math.sqrt((x2-x1)**2 + (y2-y1)**2)
  radiussum = r1 + r2 - 0.000002
  return dbetween < radiussum

def attempt(sofar, currindex):
  if currindex == n:
    return sofar
  else:
    currr = reaches[currindex]
    randomx = random.uniform(0, w)
    randomy = random.uniform(0, l)
    ok = True
    for c in sofar:
      if intersect(currr, randomx, randomy, c[0], c[1], c[2]):
        ok = False
        break
    if ok:
      sofar.append([currr, randomx, randomy])
      return attempt(sofar, currindex+1)
    else:
      return False
      
numcases = int(data.pop(0))
for case in range(numcases):
  print "Running case #" + str(case+1)
  n, w, l = [int(e) for e in data.pop(0).split(' ')]
  reaches = [int(e) for e in data.pop(0).split(' ')]
  done = False
  while done == False:
    done = attempt([], 0)
  outfile.write("Case #" + str(case + 1) + ": ")
  for d in done:
    outfile.write(str(d[1]) + " " + str(d[2]) + " ")
  outfile.write("\n")
