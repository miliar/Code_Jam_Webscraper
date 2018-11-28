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
    v = r_[t.split(' ')][1:].reshape(-1,2)
    out.append(v)

  return out


def computeTravelTimes(x):
  if len(x) == 0:
    return x
  
  strt = r_[1,x[:-1]]
  dst = abs(x-strt)
  return dst

def solve(p):
 rr = p.T[0]
 x = p.T[1].astype('int')
 N = len(x)

 i1 = find(rr=='B')
 i2 = find(rr=='O')
 assert(len(rr) == (len(i2)+len(i1)))
   
 tt = zeros(N, dtype='int')

 tt[i1] = computeTravelTimes(x[i1])
 tt[i2] = computeTravelTimes(x[i2])

 totalTime = tt[0]+1
 prev      = rr[0]
 bonus     = totalTime

 for r,t in zip(rr[1:],tt[1:]):
   if prev == r:
     #print "same robot", t
     bonus     += (t + 1)
     totalTime += (t + 1)
   else :
     t = max(0, t - bonus)
     #print "other", t
     bonus = t + 1
     totalTime += (t + 1)
   prev = r
   
 return totalTime

if __name__ == "__main__":
  import sys
  
  problem = load(sys.argv[1])
   
  for p,i in zip(problem,range(len(problem))):
    r = solve(p)
    print "Case #%d: %d" % (i+1,r)
