#!/usr/bin/env python

T = int(raw_input())

def read_problem():
  smax, shy = raw_input().split()
  smax = int(smax)
  return smax, shy

def solve(problem):
  smax, shy = problem
  standing = 0
  add = 0
  for i in range(smax+1):
    here = int(shy[i])
    if here == 0:
      continue
    if standing < i:
      diff = i - standing
      add += diff
      standing += diff
    standing += here
  return str(add)

for n in range(T):
  problem = read_problem()
  solution = solve(problem)
  print 'Case #%d: %s' %(n+1, solution)

