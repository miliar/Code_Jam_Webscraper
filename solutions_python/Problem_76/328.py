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

  pp = r_[txt[1:]].reshape(-1,2).T[1]

  for p in pp:
    out.append(r_[p.split(' ')].astype('int'))
  

  return out

def solve(p):
  ss = 0
  
  for x in p:
    ss = ss^x

  if ss == 0:
   return (sum(p) - min(p))

  return None
    

if __name__ == "__main__":
  import sys
  
  problem = load(sys.argv[1])
  pp = solve(problem[0])
  
  for p,i in zip(problem,range(len(problem))):
    r = solve(p)
    if r == None:
      print "Case #%d: NO" % (i+1)
    else :
      print "Case #%d: %d" % (i+1,r)

  
