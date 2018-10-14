#!/usr/bin/env python3

from sys import stdin, stdout, stderr

def subsets_with(N, n):
  if N == 0:
    yield {n}
  else:
    for s in subsets_with(N - 1, n):
      yield s
      yield s | {N - 1}

#for s in subsets_with(3, 1):
#  print(s)

def direction(a, b, c):
    return (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])

def convext_hull(points):
  points.sort()
  lower = list()
  upper = list()
  for p in points:
    while len(lower) >= 2 and direction(lower[-2], lower[-1], p) < 0:
      lower.pop()
    lower.append(p)
    while len(upper) >= 2 and direction(upper[-2], upper[-1], p) > 0:
      upper.pop()
    upper.append(p)
  upper.reverse()
  return lower[:-1] + upper[:-1]

def solve(N, trees):
  for i in range(N):
    m = N - 1
    for s in subsets_with(N, i):
      if trees[i] in convext_hull([trees[i] for i in s]):
        m = min(m, N - len(s))
    yield m

def main():
  T = int(input())
  for case in range(1, T + 1):
    N = int(input())
    trees = [tuple(map(int, input().split())) for i in range(N)]
    answer = solve(N, trees)
    print("Case #%d:" % case)
    for a in answer:
      print(a)

main()

