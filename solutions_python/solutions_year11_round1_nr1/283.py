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
    v = r_[t.split(' ')].astype('int')
    out.append(v)

  return out


def solve(p):
  from fractions import gcd
  N,PD,PG = p

  if PG == 100 and PD < 100:
    return 0

  if PG == 0 and PD > 0:
    return 0

  if PD == 100 or PD == 0:
    return 1

  
  assert(PD >0 and PD < 100)
  gc = gcd(100,100-PD)

  step = 100/gc

  if step > N:
    return 0

  #print N,PD,PG, gc
  #print "possible solution:", step*PD/100., step*(100-PD)/100.
  
  return 1

if __name__ == "__main__":
  import sys
  
  problem = load(sys.argv[1])
  msg = ["Broken","Possible"]
   
  for p,i in zip(problem,range(len(problem))):
    r = solve(p)
    print "Case #%d: %s" % (i+1,msg[r])
