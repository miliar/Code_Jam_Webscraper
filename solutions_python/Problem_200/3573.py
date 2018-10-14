#! /usr/bin/env python

import sys

def parse(lines):
  n = int(lines[0])
  nums = []
  for i in range(n):
    nums.append(int(lines[i+1]))
  return nums
  
def solve(num):
  last = 1
  for i in range(num):
    actNum = i + 1
    numStr = list(str(actNum))
    if sorted(numStr) == numStr:
      last = actNum
  return last
    
with open(sys.argv[1], 'r') as f:
  nums = parse(f.read().splitlines())
for i in range(len(nums)):
  sol = solve(nums[i])
  print "Case #" + str(i+1) + ": " + str(sol)
