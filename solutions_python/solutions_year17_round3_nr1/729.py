import sys
import math

def area(t):
  tuples = sorted(t, key=lambda tup: -tup[0])
  return math.pi * ( tuples[0][0] ** 2 + 2 * sum([tup[0] * tup[1] for tup in tuples]))

def maxarea(t, k):
  tuples = sorted(t, key=lambda tup: -(tup[0]**2 + 2 *tup[1]*tup[0]))
  to_compute = [tuples.pop(0)] + sorted(tuples, key=lambda tup: -(tup[0] * tup[1]))
  #print to_compute[0:k]
  #return '%f' % (area(to_compute[0:k]))
  return area(to_compute[0:k])

ct = 0
while True:
  line = sys.stdin.readline()
  if not line: break
  ct += 1
  if ct == 1:
    continue
  parts = line.split(' ')
  n = int(parts[0])
  k = int(parts[1])
  t = []
  for i in xrange(0, n):
    l = sys.stdin.readline()
    p = l.split(' ')
    t.append((int(p[0]), int(p[1])))
  print("Case #{0}: {1}".format(ct-1, maxarea(t,k)))

