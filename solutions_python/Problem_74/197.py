#!/usr/bin/python

import sys

def solveCase(case):
  p = {'O':1,'B':1}
  t = {'O':0,'B':0}
  for step in case:
    key = step[0]
    position = int(step[1])
    t[key] += abs(p[key]-position)
    t[key] = max(t.values())+1
    p[key] = position
    #print step,t,p
  return max(t.values())

data="""3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1""".split("\n")

n=0
for row in sys.stdin:
  if n:
    rowArray = row.split(' ')[1:]
    print "Case #%s: %s" % (n,solveCase(zip(rowArray[0::2],rowArray[1::2])))
  n=n+1

