#!/usr/bin/env python3

import collections
import sys

N = 2000

print("Allocating...", file=sys.stderr)
choose = [[0 for i in range(N + 1)] for j in range(N + 1)]
print("Preprocessing...", file=sys.stderr)
for n in range(N + 1):
    choose[n][0] = 1
    choose[n][n] = 1
for n in range(1, N + 1):
    for k in range(1, n):
        choose[n][k] = (choose[n - 1][k - 1] + choose[n - 1][k])

def sim(N, X, Y, heights):
  pyramid = 0
  step = 0
  while pyramid + 4 * step + 1 <= N:
    pyramid += 4 * step + 1
    step += 1
#  print(pyramid, step, N)
  if X + Y <= 2 * step - 1 and Y - X <= 2 * step - 1:
    return 1
  if not (X + Y <= 2 * (step + 1) - 1 and Y - X <= 2 * (step + 1) - 1):
    return 0
  if X == 0:
    return 0
  remaining = N - pyramid
#  print(step)
  side = 2 * step
#  print(Y, side, remaining)
  if side <= remaining:
    if Y < remaining - side:
      return 1
    Y, side, remaining = Y - (remaining - side), 2 * side - remaining, remaining - 2 * (remaining - side)
#  print(Y, side, remaining)
  a = sum(choose[remaining][i] for i in range(Y + 1, remaining + 1))
  b = 2 ** remaining
#  print(a, b)
  return a / b
    

def solve(X, Y, N): 
  heights = collections.defaultdict(lambda _: 0)
  return sim(X, Y, N, heights)

def main():
  T = int(input())
  for case in range(1, T + 1):
    N, X, Y = map(int, input().split())
    print("Case #%d: %.8f" % (case, solve(N, X, Y)))

if __name__ == "__main__":
  main()

