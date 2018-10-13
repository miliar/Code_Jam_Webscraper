#!/usr/bin/env python3

import sys

def solve(problem):
  row1, grid1, row2, grid2 = problem
  solutions = set(grid1[row1 - 1]) & set(grid2[row2 - 1])
#  print(solutions, file=sys.stderr)
  if len(solutions) == 0:
    return "Volunteer cheated!"
  elif len(solutions) == 1:
    return solutions.pop()
  else:
    return "Bad magician!"

def read():
  row1 = int(input())
  grid1 = [list(map(int, input().split())) for i in range(4)]
  row2 = int(input())
  grid2 = [list(map(int, input().split())) for i in range(4)]
  return (row1, grid1, row2, grid2)

def main():
  cases = int(input())
  for i in range(cases):
    problem = read()
    print("Case #%d: %s" % (i + 1, solve(problem)))

if __name__ == "__main__":
  main()

