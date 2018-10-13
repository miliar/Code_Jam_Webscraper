#!/usr/bin/env python

from sys import stdin, stdout, stderr

from pulp import *



def solve(N, V, X, sources):
  problem = LpProblem("problem", LpMinimize)
  R = [sources[i][0] for i in range(N)]
  C = [sources[i][1] for i in range(N)]
  T = [LpVariable("T%d" % i) for i in range(N)]
  M = LpVariable("M")

  problem += M
  problem += lpSum(T[i] * R[i] for i in range(N)) == V
  problem += lpSum(T[i] * R[i] * C[i] for i in range(N)) == X * V
  for i in range(N):
    problem += M >= T[i]

  PULP_CBC_CMD().solve(problem)

  lower_than_all = True
  higher_than_all = True
  for i in range(N):
    if C[i] <= X:
      lower_than_all = False
    if C[i] >= X:
      higher_than_all = False
  if lower_than_all or higher_than_all:
    return "IMPOSSIBLE"

  return value(problem.objective)

def main():
  T = int(input())
  for case in range(1, T + 1):
    N, V, X = map(float, raw_input().split())
    N = int(N)
    sources = [map(float, raw_input().split()) for i in range(N)]
    answer = solve(N, V, X, sources)
    if answer != "IMPOSSIBLE":
      answer = "%.7f" % answer
    print("Case #%d: %s" % (case, answer))

main()

