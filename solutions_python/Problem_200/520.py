from sys import stdin
from collections import defaultdict

T = int(stdin.readline())

for t in range(T):
  N = int(stdin.readline())
  Z = 0
  C = 0
  i = 0

  while (10 ** (i + 1)) <= N:
    X = N // (10 ** i) % 10
    Y = N // (10 ** (i + 1)) % 10

    if X - C < Y:
      Z = i + 1
      C = 1
    else:
      C = 0
    i += 1
  if Z:
    N -= (N % 10 ** Z) + 1

  print("Case #%d: %d" % (t + 1, N))
