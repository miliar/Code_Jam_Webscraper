import math
import itertools
import sys

FILENAME = 'A-large'

def something_in_dir(grid, d, i, j):
  if d == '^':
    change = (-1, 0)
  elif d == 'v':
    change = (1, 0)
  elif d == '>':
    change = (0, 1)
  elif d == '<':
    change = (0, -1)
  new_i = i + change[0]
  new_j = j + change[1]
  while True:
    if (new_i < 0 or new_i >= len(grid) or new_j < 0 or new_j >= len(grid[0])):
      return False
    if grid[new_i][new_j] != '.':
      return True
    new_i = new_i + change[0]
    new_j = new_j + change[1]


f = open(FILENAME + '.in', 'r')
tests = int(f.readline())
sys.stdout = open(FILENAME + '.out', 'w')
for test in range(tests):
  r, c = map(int, f.readline().split())
  grid = []
  for i in range(r):
    grid.append(list(f.readline().strip()))
  changes = 0
  bad = False
  for i in range(r):
    for j in range(c):
      if grid[i][j] != '.':
        d = grid[i][j]
        if something_in_dir(grid, d, i, j):
          continue

        if not something_in_dir(grid, '^', i, j) and \
           not something_in_dir(grid, 'v', i, j) and \
           not something_in_dir(grid, '>', i, j) and \
           not something_in_dir(grid, '<', i, j):
          bad = True
          break
        changes += 1
    if bad:
      break
  if bad:
    print 'Case #%d: IMPOSSIBLE' % (test + 1)
  else:
    print 'Case #%d: %d' % (test + 1, changes)


