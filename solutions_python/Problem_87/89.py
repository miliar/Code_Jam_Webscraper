#!/usr/bin/python
from numpy import *
from pylab import find

def readLines(fname):
  with open(fname,'r') as f :
    lines = r_[[ s[:-1] for s in f.readlines() ]]
    return lines

  return None

def load(fname):
  txt = readLines(fname)
  nc  = int(txt[0])
  out = []

  i = 1
  while i < len(txt):
    l = txt[i]
    X,S,R,t,N = r_[l.split(' ')].astype(uint32)

    ww = r_[ [ r_[l.split(' ')].astype(uint32) for l in txt[i+1:(i+1+N) ] ] ]

    v = (X,S,R,t,ww)

    i = i + N  + 1
    out.append(v)

  assert(len(out) == nc)
  return out

def solve(p):
  X,S,R,t,ww = p

  #print X,S,R,t
  #print ww
  L = r_[ [ w[1] - w[0] for w in ww ] ]
  w = r_[ [ c[2] for c in ww ] ]

  ii = argsort(w)
  L = L[ii]
  w = w[ii]

  nw = X - sum(L)
  #print "no walkway",nw

  if nw > 0:
    L = r_[ nw, L]
    w = r_[ 0, w]

  trun = double(t)
  tt   = 0.0
  L    = L.astype(float64)
  w    = w.astype(float64)

  #print "w:",w
  #print "L:",L

  for i in xrange(len(L)):
    #print L[i], w[i], tt
    if trun > 0 :
      tr = L[i]/(w[i] + R)
      if tr <= trun :
        #print "ran all"
        trun -= tr
        t = tr
      else :
        #print "ran some", trun, tr
        t = trun + (L[i] - trun*(w[i] + R) )/ (w[i]+S)
        trun = 0
    else :
      #print "walked"
      t = L[i]/(w[i] + S)

    tt += t

  return tt


if __name__ == "__main__":
  import sys
  
  problem = load(sys.argv[1])
   
  for p,i in zip(problem,range(len(problem))):
    r = solve(p)
    print "Case #%d: %.12f" % (i+1,r)
