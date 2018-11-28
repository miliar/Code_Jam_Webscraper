#!/usr/bin/env python

from numpy import *
from math import sqrt,ceil,floor

def area(n,b):
  return (n+1)*(2*n + b)
  
def solve(p):
  r,t = p
  b = 2*r + 1
  n = int(floor((sqrt(b*b - 4*b +8*t + 4) - b - 2)/4))

  if area(n,b) <= t :
    return str(n+1)
  
  return str(n)

  

def load_case(ll):
  p = [int(l) for l in ll[0].split(" ")]
  rst = ll[1:]
  return p,rst

################################################################################
# Support code below
################################################################################

def slurp(fname):
  with open(fname,"r") as f:
    l = f.readline()
    while l:
      yield l[:-1]
      l = f.readline()

def load_problems(fname):
  ll = r_[ [l for l in slurp(fname)] ]
  N = int(ll[0])

  rst = ll[1:]
  for i in xrange(N):
    p,rst = load_case(rst)
    yield (i+1,p)

  
if __name__ == "__main__":
  import sys
  fname = sys.argv[1]

  base = fname.split(".")[0]
  fout = open(base+".out","w")

  def sink(s):
    print s
    fout.write(s+"\n")
  
  for i,p in load_problems(fname):
    r = solve(p)
    sink( "Case #%d: %s" % (i,r) )

  fout.close()
