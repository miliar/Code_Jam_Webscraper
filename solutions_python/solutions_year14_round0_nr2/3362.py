from sys import *

def getNextVal(C, F, X, n):
  t = 0
  ck = 2
  for i in range(n):
    t += 1.0 * C / ck
    ck += F

  t += 1.0 * X / ck
  return t

def solve(inp1):
  C = inp1[0]
  F = inp1[1]
  X = inp1[2]

  prevVal = 99999999
  i = 0
  nextVal = getNextVal(C, F, X, i)
  while nextVal < prevVal:
    i += 1
    prevVal = nextVal
    nextVal = getNextVal(C, F, X, i)
  return prevVal

cases = int(raw_input())
for _ in xrange(cases):
  inp1 = map(float, stdin.readline().split())
  res = solve(inp1)

  print "Case #%d:" %(_+1), res
