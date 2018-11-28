# -*- coding: utf-8 -*-

import sys

def readInts():
  line = sys.stdin.readline().rstrip("\n")
  return map(int,line.split(" "))

RICHARD="RICHARD"
GABRIEL="GABRIEL"

def solve(X,R,C):
  if (R*C) % X != 0:
    return RICHARD
  if X == 1 or X == 2:
    return GABRIEL
  elif X == 3:
    if min(R,C) == 1:
      return RICHARD
    else:
      return GABRIEL
  else:
    if min(R,C) >= 3 and max(R,C) >= 4:
      return GABRIEL
    else:
      return RICHARD

def main():
  T = readInts()[0]
  for t in xrange(1, T+1):
    X,R,C = readInts()
    ans = solve(X,R,C)
    print "Case #%d: %s"%(t, ans)

if __name__ == "__main__":
  main()
