#! /usr/bin/env python

import sys

def parse(lines):
  n = int(lines[0])
  nums = []
  for i in range(n):
    nums.append((int(lines[i+1].split(" ")[0]), int(lines[i+1].split(" ")[1])))
  return nums
  
def computeLeftRight(stalls, s):
  left = 0
  right = 0
  for i in range(s+1, len(stalls)):
    if stalls[i]:
      right = right + 1
    else:
      break
  for i in reversed(range(0, s)):
    if stalls[i]:
      left = left + 1
    else:
      break
  return (left, right)
  
def solve(num):
  n = num[0]
  k = num[1]
  stalls = []
  for i in range(n+2):
    stalls.append(True)
  stalls[0] = False
  stalls[n+1] = False
  for j in range(k):
    maxVal = 0
    minVal = 0
    best = 0
    for s in range(1, n+1):
      if stalls[s]:
        leftRight = computeLeftRight(stalls, s)
        if (min(leftRight[0], leftRight[1]) > minVal):
          minVal = min(leftRight[0], leftRight[1])
          maxVal = max(leftRight[0], leftRight[1])
          best = s
        elif (min(leftRight[0], leftRight[1]) == minVal and max(leftRight[0], leftRight[1]) > maxVal):
          minVal = min(leftRight[0], leftRight[1])
          maxVal = max(leftRight[0], leftRight[1])
          best = s
    stalls[best] = False
  return str(maxVal) + " " + str(minVal)
    
with open(sys.argv[1], 'r') as f:
  nums = parse(f.read().splitlines())
for i in range(len(nums)):
  sol = solve(nums[i])
  print "Case #" + str(i+1) + ": " + sol
