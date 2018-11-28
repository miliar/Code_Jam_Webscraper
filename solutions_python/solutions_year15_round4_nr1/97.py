#!/usr/bin/env python3

from sys import stdin, stdout, stderr

direction = {
  "^": (-1, 0),
  ">": (0, 1),
  "v": (1, 0),
  "<": (0, -1),
}

def falls(R, C, grid, i, j, di, dj):
  while True:
    i += di
    j += dj
    if 0 <= i < R and 0 <= j < C:
      if grid[i][j] != ".":
        return False
    else:
      return True

def solve(R, C, grid):
  counter = 0
  for i in range(R):
    for j in range(C):
      if grid[i][j] != ".":
        di, dj = direction[grid[i][j]]
        if falls(R, C, grid, i, j, di, dj):
          impossible = True
          for (di, dj) in direction.values():
            if not falls(R, C, grid, i, j, di, dj):
              impossible = False
          if impossible:
            return "IMPOSSIBLE"
          else:
            counter += 1
  return counter

def main():
  T = int(input())
  for case in range(1, T + 1):
    R, C = map(int, input().split())
    grid = [list(input().strip()) for i in range(R)]
    answer = solve(R, C, grid)
    print("Case #%d: %s" % (case, answer))

main()

