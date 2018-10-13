#! /usr/bin/python
import sys

INFILE= sys.argv[1]


def time2reach(farm, cost, amount, rate):
  r = 2
  t=0.0
  for i in xrange(farm):
    t+=cost/r
    r += rate

  t+=amount/r
  return t

#print time2reach(4, 500, 2000, 4.0)


with open(INFILE) as f:
  nTestCase = int( f.readline() )
  caseNo = 0
  while caseNo < nTestCase:
    (C, F, X) = (float(x) for x in f.readline().split())
    caseNo+=1
    seconds = 9999999999
    farm=0
    while True:
      t = time2reach(farm, C, X, F)
      if t < seconds:
        seconds = t
        farm+=1
      else:
        break;

    print "Case #%s: %s"%(caseNo, seconds)




