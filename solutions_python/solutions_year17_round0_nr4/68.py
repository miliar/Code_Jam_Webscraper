#!/usr/bin/env python3

from heapq import heappush, heappop

def process(N, pawns, bishops):
  def pawnfilter(s, r, c):
    for i, j in s:
      if i != r and j != c:
        yield i, j
  def bishopfilter(s, r, c):
    for i, j in s:
      if i+j != r+c and i-j != r-c:
        yield i, j
  def edgedist(p):
    r, c = p
    return min(r, c, N-1-r, N-1-c)
  free = ((i, j) for i in range(N) for j in range(N))
  for i, j in pawns:
    free = pawnfilter(free, i, j)
  try:
    while True:
      i, j = next(free)
      pawns.add((i, j))
      free = pawnfilter(free, i, j)
  except StopIteration:
    pass
  free = ((i, j) for i in range(N) for j in range(N))
  for i, j in bishops:
    free = bishopfilter(free, i, j)
  try:
    while True:
      free = list(free)
      i, j = min(free, key=edgedist)
      bishops.add((i, j))
      free = bishopfilter(free, i, j)
  except ValueError:
    pass
  return pawns, bishops

T = int(input())
for case in range(1, T+1):
  N, M = map(int, input().split())
  pawns = set()
  bishops = set()
  for i in range(M):
    t, r, c = input().split()
    r, c = int(r)-1, int(c)-1
    if t == 'x' or t == 'o':
      pawns.add((r, c))
    if t == '+' or t == 'o':
      bishops.add((r, c))
  p, b = process(N, set(pawns), set(bishops))
  mod = (p-pawns) | (b-bishops)
  print("Case #{}: {} {}".format(case, len(p)+len(b), len(mod)))
  for r, c in mod:
    t = 'x' if (r, c) in p else ''
    t += '+' if (r, c) in b else ''
    if t == 'x+': t = 'o'
    print("{} {} {}".format(t, r+1, c+1))

