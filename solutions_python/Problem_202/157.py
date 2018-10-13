#!/usr/bin/python

from sys import stdin as I

def intersections(X, Y, N):
  m = min(X, Y)
  yield (X-m, Y-m)
  m = min(N-1-X, Y)
  yield (X+m, Y-m)
  m = min(X, N-1-Y)
  yield (X-m, Y+m)
  m = min(N-1-X, N-1-Y)
  yield (X+m, Y+m)

def solve(T):
  N, M = map(int, I.readline().split())

  border = set()
  border.update([(x, y) for x in [0, N-1] for y in range(N)])
  border.update([(x, y) for y in [0, N-1] for x in range(N)])

  columns = set(range(N))
  rows = set(range(N))

  grid = {}

  for m in range(M):
    V, X, Y = I.readline().split()
    X, Y = int(X)-1, int(Y)-1
    grid[(X, Y)] = V if V != 'o' else 'oo'
    if V == 'x' or V == 'o':
      columns.discard(X)
      rows.discard(Y)
    if V == '+' or V == 'o':
      border.difference_update(intersections(X, Y, N))

  updated = set()

  while len(columns) > 0 and len(rows) > 0:
    X, Y = columns.pop(), rows.pop()
    v = grid.get((X, Y), '')
    grid[(X, Y)] = v + 'x'
    updated.add((X, Y))

  while len(border) > 0:
    X, Y = border.pop()
    border.difference_update(intersections(X, Y, N))
    v = grid.get((X, Y), '')
    grid[(X, Y)] = v + '+'
    updated.add((X, Y))

  score = sum([len(v) for v in grid.values()])
  print("Case #%i: %i %i" % (T, score, len(updated)))
  for update in updated:
    char = grid[update] if len(grid[update]) == 1 else 'o'
    print("%s %i %i" % (char, update[0]+1, update[1]+1))

T = int(I.readline())
for t in range(1, T + 1):
  solve(t)
