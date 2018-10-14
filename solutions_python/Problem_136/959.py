#!/bin/python
from __future__ import division
import sys



def readin(infile):
  print >> sys.stderr, "reading from " + infile
  lines=open(infile, 'r').readlines()
  testcount = int(lines[0])
  dropped=0
  while lines[-1]=='':
    lines=lines[:-1]
    dropped+=1
  print >> sys.stderr, "read %d test cases from %d lines (%d dropped)"%(testcount, len(lines), dropped)
  lines=lines[1:]
  return testcount, lines

def doall(testcases, lines):

  for case, line in enumerate(lines):
    line=line.split()
    c = float(line[0])
    f = float(line[1])
    x = float(line[2])

    t=solve(c,f,x)
    print 'Case #%d: %.7f'%(case+1,t)

def solve(cost,farmrate,goal):

  t, cookies, rate = 0,0,2 
  while True:
    #if I just run from here:
    finaltime1 = t + (goal-cookies)/rate
    #if I buy a farm:
    farmtimeinterval = (cost-cookies)/rate
    farmtimeinterval = max(0, farmtimeinterval)

    finaltime2 = t + farmtimeinterval + goal/(rate+farmrate) 

    #do the best
    if finaltime1 <= finaltime2:
      return finaltime1

    t+= farmtimeinterval
    rate+=farmrate
    cookies=0

if __name__ == '__main__': 
  if len(sys.argv) != 2:
    print >> sys.stderr, "bad args"
    sys.exit(1)
  tc, l = readin(sys.argv[1])
  doall(tc, l)
  print >> sys.stderr, "done"

