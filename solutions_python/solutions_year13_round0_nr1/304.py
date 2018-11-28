#!/usr/bin/env python

from numpy import *

def slurp(fname):
  with open(fname,"r") as f:
    l = f.readline()
    while l:
      yield l[:-1]
      l = f.readline()

def load(fname):
  ll = r_[ [l for l in slurp(fname)] ]
  N = int(ll[0])
  ll = ll[1:].reshape(N,5)[:,:-1]

  return ll


def make_lookup_table():
    ii = r_[ range(16) ].reshape(4,4)
    r = []
    r.extend([ i for i in ii ])
    r.extend([ i for i in ii.T] )
    r.extend([diag(ii), diag(ii[::-1,:])])
    return r

tbl = make_lookup_table()

def solve(p):
  def check_winner(x):
    if x.replace("T","X") == "XXXX": return "X"
    if x.replace("T","O") == "OOOO": return "O"
    return None

  b = "".join(p)
  xs = [ "".join([b[i] for i in t ]) for t in tbl]

  for x in xs:
    w = check_winner(x)
    if w:
      return "%s won" % (w)

  if b.count(".") == 0: return "Draw"

  return "Game has not completed"


if __name__ == "__main__":
  import sys
  
  problem = load(sys.argv[1])

  for i,p in enumerate(problem,1):
    r = solve(p)
    print "Case #%d: %s" % (i,r)
