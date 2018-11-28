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
    v  = r_[t.split(' ')]

    C  = int(v[0])
    v  = v[1:]
    ss = v[:C]
    v  = v[C:]

    D  = int(v[0])
    v  = v[1:]
    oo = v[:D]
    v  = v[D:]

    N  = int(v[0])
    v  = v[1:]
    s  = v[0]
    
    out.append([ss,oo,s])

  return out

def checkMerge(mm,ll):
  if len(ll) < 2:
    return False

  s = ll[-2]+ll[-1]

  if mm.has_key(s) :
    ll.pop()
    ll[-1] = mm[s]
    return True
    
  return False

def checkClear(om, ll):
  if len(ll) < 2:
    return False

  if om.has_key(ll[-1]):
    s = om[ll[-1]]

    rr = s.intersection(set(ll[:-1]))

    if len(rr) > 0:
      return True

  return False

def solve(p):
  ss,oo,txt = p[:3]

  mm = {}
  om = {}

  for s in ss:
    mm[s[:2]] = s[2]
    mm[s[1]+s[0]] = s[2]

  for s in oo:
    k1,k2 = s[:2]
    if om.has_key(k1) == False :
      om[k1] = set()

    if om.has_key(k2) == False :
      om[k2] = set()

    om[k1].add(k2)
    om[k2].add(k1)

  #print "merge set",mm
  #print "oppose set",om
  #print txt
  
  ll = []

  for k in txt:
    ll.append(k)
    while checkMerge(mm,ll) == True:
      pass

    if checkClear(om,ll) :
      ll = []
    
  return ll

def fmtSet(ll):
  s = '['
  N = len(ll)

  for k,i in zip(ll, range(N)):
    s = s + "%s"%(k)

    if i+1 != N:
      s = s + ", "

  s = s + "]"
  return s

if __name__ == "__main__":
  import sys
  
  problem = load(sys.argv[1])
   
  for p,i in zip(problem,range(len(problem))):
    r = solve(p)
    print "Case #%d: %s" % (i+1, fmtSet(r))
