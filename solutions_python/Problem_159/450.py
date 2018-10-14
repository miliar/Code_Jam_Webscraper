# -*- coding: utf-8 -*-

import sys

def readInts():
  line = sys.stdin.readline().rstrip("\n")
  return map(int,line.split(" "))

def solve(N, ms):
  # first
  ans1 = 0
  maxReduction = 0
  for i in xrange(1, N):
    if ms[i] - ms[i-1] < 0:
      ans1 += ms[i-1] - ms[i]
      if ms[i-1] - ms[i] > maxReduction:
        maxReduction = ms[i-1] - ms[i]

  ans2 = 0
  if maxReduction == 0:
    return ans1, ans2

  for i in xrange(0, N-1):
    ans2 += min(ms[i], maxReduction)

  return ans1, ans2
    

def main():
  T = readInts()[0]
  for t in xrange(1,T+1):
    N = readInts()[0]
    ms = readInts()
    
    y,z = solve(N, ms)
    
    print "Case #%d: %d %d"%(t, y, z)
  

if __name__ == "__main__":
  main()
