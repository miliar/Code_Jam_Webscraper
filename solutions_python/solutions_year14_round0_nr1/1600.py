#!/usr/bin/env python

T = int(raw_input())

def read_problem():
  a0 = int(raw_input())
  b0 = []
  b0.append([ int(e) for e in raw_input().split() ])
  b0.append([ int(e) for e in raw_input().split() ])
  b0.append([ int(e) for e in raw_input().split() ])
  b0.append([ int(e) for e in raw_input().split() ])
  a1 = int(raw_input())
  b1 = []
  b1.append([ int(e) for e in raw_input().split() ])
  b1.append([ int(e) for e in raw_input().split() ])
  b1.append([ int(e) for e in raw_input().split() ])
  b1.append([ int(e) for e in raw_input().split() ])
  return a0, b0, a1, b1

def solve(problem):
  a0, b0, a1, b1 = problem
  r0 = b0[a0-1]
  r1 = b1[a1-1]
  r = set(r0) & set (r1)
  if len(r) == 1:
    return r.pop()
  elif len(r) == 0:
    return 'Volunteer cheated!'
  else:
    return 'Bad magician!'

for n in range(T):
  problem = read_problem()
  solution = solve(problem)
  print 'Case #%d: %s' %(n+1, solution)

