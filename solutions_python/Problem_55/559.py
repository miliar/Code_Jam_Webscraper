#!/local/usr/bin/python2.5

import sys

def roll(R, k, g):
  euro, curr = 0, []
  for i in range(R):
    while 1:
      if len(g)==0 or sum(curr)+g[0] > k: break
      curr.append(g.pop(0))
    euro += sum(curr)
    g += curr
    curr = []
  return euro

T = int(sys.stdin.readline().strip())

for i in range(T):
  R, k = [int(x) for x in sys.stdin.readline().split()[:2]]
  g = [int(j) for j in sys.stdin.readline().split()]
  print 'Case #%d: %d' % (i+1, roll(R,k,g))
