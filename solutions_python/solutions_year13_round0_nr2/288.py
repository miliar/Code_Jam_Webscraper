#!/usr/bin/env python

from numpy import *

def slurp(fname):
  with open(fname,"r") as f:
    l = f.readline()
    while l:
      yield l[:-1]
      l = f.readline()

def ints(l):
  return [int(x) for x in l.split(" ") if x != ""]


def load(fname):
  ll = [ints(l) for l in slurp(fname)]
  N  = ll[0][0]
  ll = ll[1:]

  pp = []
  for i in xrange(N):
    N,M = ll[0]
    p = r_[ ll[1:(N+1)] ]
    pp.append(p)
    ll = ll[(N+1):]
  return pp
  

def solve(p):
  c_max = p.max(0)
  r_max = p.max(1)

  N,M = p.shape

  for r in xrange(N):
    for c in xrange(M):
      v = p[r,c]
      if v < r_max[r] and v < c_max[c]:
        return "NO"

  return "YES"


if __name__ == "__main__":
  import sys
  
  problem = load(sys.argv[1])

  for i,p in enumerate(problem,1):
    r = solve(p)
    print "Case #%d: %s" % (i,r)

