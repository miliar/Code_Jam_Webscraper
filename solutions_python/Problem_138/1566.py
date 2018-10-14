#!/usr/bin/env python

import sys
import bisect

def main():
  f = sys.stdin
  caseCount = int(f.readline().strip())
  for i in xrange(1, caseCount+1):
    n, b1s, b2s = getInput(f)
    dScore, nScore = solve(n, b1s, b2s)
    displayAndClear(i, dScore, nScore)

def getInput(f):
  n = int(f.readline().strip())
  b1s = [float(arg) for arg in f.readline().split()]
  b2s = [float(arg) for arg in f.readline().split()]
  return n, b1s, b2s

def displayAndClear(i, dScore, nScore):
  print 'Case #%d: %d %d' % (i, dScore, nScore)

def solve(n, b1s, b2s):
  nScore = playNormal(n, b1s, b2s)
  dScore = playDeceitful(n, b1s, b2s)
  return dScore, nScore

def playNormal(n, b1List, b2List):
  b1s = sorted(b1List)
  b2s = sorted(b2List)

  score = 0
  for b1 in b1s:
    pos = bisect.bisect_left(b2s, b1)
    if pos == len(b2s):
      b2 = b2s.pop(0) #TODO: blist, deque
    else:
      b2 = b2s.pop(pos) # infeasible

    #print b1, b2
    if b1 > b2:
      score += 1
  return score

def playDeceitful(n, b1List, b2List):
  b1s = sorted(b1List)
  b2s = sorted(b2List)
  
  score = 0
  while len(b1s) > 0:
    if b1s[-1] < b2s[-1]:
      b2 = b2s.pop()
      b1 = b1s.pop(0) #TODO: blist
    else:
      b2 = b2s.pop()
      b1 = b1s.pop()
      score += 1

  return score

if __name__ == '__main__':
  main()


