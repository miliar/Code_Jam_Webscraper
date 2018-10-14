#!/usr/bin/env python

T = int(raw_input())

def read_problem():
  N, M = [int(e) for e in raw_input().split()]
  pattern = []
  for i in range(N):
    pattern.append([int(e) for e in raw_input().split()])
  return N, M, pattern

def solve(problem):
  N, M, pattern = problem
  max_i = [max(line) for line in pattern]
  max_j = [max([line[i] for line in pattern]) for i in range(M)]
  for i in range(N):
    for j in range(M):
      v = pattern[i][j]
      if v < max_i[i] and v < max_j[j]:
        return 'NO'
  return 'YES'

for n in range(T):
  problem = read_problem()
  solution = solve(problem)
  print 'Case #%d: %s' %(n+1, solution)

