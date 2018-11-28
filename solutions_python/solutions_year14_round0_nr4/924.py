#!/bin/python
from __future__ import division
import sys



def readin(infile):
  print >> sys.stderr, "reading from " + infile
  lines=open(infile, 'r').readlines()
  testcount = int(lines[0])
  dropped=0
  while lines[-1].strip()=='':
    lines=lines[:-1]
    dropped+=1
  print >> sys.stderr, "read %d test cases from %d lines (%d dropped)"%(testcount, len(lines), dropped)
  lines=lines[1:]
  return testcount, lines

def doall(testcases, lines):

  case = 1
  while lines:
    n=int(lines[0])
    naomi = [float(v) for v in lines[1].split()]
    ken = [float(v) for v in lines[2].split()]
    assert len(ken)==n
    assert len(naomi)==n
    lines=lines[3:]

    d, w = solve(n, naomi, ken)
    print 'Case #%d: %d %d'%(case, d, w)
    case +=1

def solve(n, naomi, ken):
  naomi=sorted(naomi)
  ken=sorted(ken)
  n=naomi[:]
  k=ken[:]
  warwin=0
  while n:
    if n[-1]>k[-1]:
      warwin+=1
      k=k[1:]
    else:
      k=k[:-1]
    n=n[:-1]


  dwarwin=0
  while naomi:
    if naomi[0] > ken[0]:
      #if a sure win, take it
      naomi=naomi[1:]
      ken=ken[1:]
      dwarwin+=1
    else:
      #n will lose, use smallest and lie to lose big
      naomi=naomi[1:]
      ken=ken[:-1]


  return dwarwin,warwin










if __name__ == '__main__': 
  if len(sys.argv) != 2:
    print >> sys.stderr, "bad args"
    sys.exit(1)
  tc, l = readin(sys.argv[1])
  doall(tc, l)
  print >> sys.stderr, "done"

