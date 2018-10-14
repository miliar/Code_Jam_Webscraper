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
    t = txt[i]
    R,C,D = r_[t.split(' ')].astype(uint32)

    w = r_[ [ [ord(c) - ord('0') for c in t ] for t in txt[i+1:i+1+R]] ]

    i = i + R  + 1
    out.append( (w,D) )

  assert(nc == len(out))
  return out


def checkBlade(a):
  K = a.shape[0]

  #take corners out
  a = a.copy()
  a[0,0] = a[0,-1] = a[-1,0] = a[-1,-1] = 0

  if K % 2 == 0: #Even
    x =  arange( -(K-1),K,2)
  else :
    x = arange(-(K/2),K/2+1)

  mx = sum(sum(x*a[i]) for i in xrange(K))
  if mx != 0:
    return False
  my = sum(sum(x*a[:,i]) for i in xrange(K))

  return (my == 0)
    
def checkSize(w,K):
  sz = w.shape
  for i in xrange(0,sz[0] - K+1):
    for j in xrange(0,sz[1]-K+1):
      if checkBlade(w[i:i+K, j:j+K]) :
        return True
  return False

def solve(p):
  w,D = p
  ss = min(w.shape)

  for K in xrange(ss,2,-1):
    if checkSize(w,K) :
      return K
    
  return 0


if __name__ == "__main__":
  import sys
  
  problem = load(sys.argv[1])
   
  for p,i in zip(problem,range(len(problem))):
    r = solve(p)
    if r :
      print "Case #%d: %d" % (i+1,r)
    else :
      print "Case #%d: IMPOSSIBLE" % (i+1)
