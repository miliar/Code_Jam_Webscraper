#!/usr/bin/env python3

def solve(shy_max, shy_levels):
  shy_levels = list(map(int, shy_levels))
  standing = 0
  needed = 0
  for level in range(shy_max + 1):
    if shy_levels[level] > 0:
      if standing < level:
        needed += max(0, level - standing)
        standing = level
      standing += shy_levels[level]
  return needed

T = int(input())
for case in range(1, T + 1):
  shy_max, shy_levels = input().split()
  shy_max = int(shy_max)
  answer = solve(shy_max, shy_levels)
  print("Case #%d: %s" % (case, answer))
  
