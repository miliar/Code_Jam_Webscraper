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
  
  for t in txt[1:]:
    v = r_[t.split(' ')].astype('int64')
    p1 = v[:3]
    C  = v[3]
    aa = v[4:]
    assert(len(aa) == C)
    out.append([p1,aa])

  return out

def computeStarDistances(N,aa):
  cc = r_[list(aa)*(1+N/len(aa))][:N]
  return cc

def solve(p):
  L,t,N = p[0]
  aa = p[1]

  #print L,t,N
  #print aa

  cc = computeStarDistances(N,aa)

  assert(len(cc) == N)
  assert(t%2 == 0)

  d0 = t/2
  cs = 0
  fs = None
  correction = None

  for i in range(len(cc)):
    cs += cc[i]
    if cs >= d0:
      fs = i
      correction = cs - d0
      break

  if fs == None:
    #print "do too large"
    #print "cc:",cc
    #print "fs:", fs, "t:", t , "d0:",d0, "corr:",correction
    return sum(cc)*2
  
  assert(fs >= 0 )
  assert(correction >= 0 )

  if  correction == 0:
    left_over = cc[(fs+1):].copy()
  else :
    left_over = cc[fs:].copy()
    left_over[0] = correction
    assert(cc[0] > 0 )

  lo = left_over
  left_over = sort(left_over)[::-1]

  total_time = t + sum(left_over[:L]) + 2*sum(left_over[L:])

  #print "cc:",cc
  #print "cc*:",lo, left_over[:L], left_over[L:]
  #print "fs:", fs, "t:", t , "d0:",d0, "corr:",correction
  
  return total_time


if __name__ == "__main__":
  import sys
  
  problem = load(sys.argv[1])
   
  for p,i in zip(problem,range(len(problem))):
    r = solve(p)
    print "Case #%d: %d" % (i+1,r)
