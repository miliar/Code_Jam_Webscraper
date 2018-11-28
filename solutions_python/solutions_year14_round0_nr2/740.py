#!/usr/bin/env python3

import sys

def solve(problem):
  C, F, X = problem
  current_time = 0.0
  current_rate = 2.0
  current_solution = current_time + X / current_rate
  while True:
#    print(current_solution, file=sys.stderr)
    next_time = current_time + C / current_rate
    next_rate = current_rate + F
    next_solution = next_time + X / next_rate
    if next_solution > current_solution:
      return current_solution
    else:
      current_time = next_time
      current_rate = next_rate
      current_solution = next_solution

def read():
  C, F, X = map(float, input().split())
  return (C, F, X)

def write(i, solution):
  print("Case #%d: %.7f" % (i + 1, solution))

def main():
  cases = int(input())
  for i in range(cases):
    problem = read()
    solution = solve(problem)
    write(i, solution)

if __name__ == "__main__":
  main()

