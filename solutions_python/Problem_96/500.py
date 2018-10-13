#!/usr/bin/env python

def solve(lst):
  N = lst[0]
  S = int(lst[1])
  P = int(lst[2])
  points = map(lambda x: int(x), lst[3:])
  total = 0
  for item in points:
    if ((item + 2) / 3) >= P:
      total += 1
      continue
    if S == 0:
      continue
    if ((item + 4) / 3) >= P and item >= P:
      total += 1
      S -= 1
  return total
    

num_of_cases = int(raw_input())

num = 1

while num <= num_of_cases:
  case = raw_input().split()
  print "Case #" + str(num) + ": " + str(solve(case))
  num += 1
