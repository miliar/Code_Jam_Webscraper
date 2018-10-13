#!/usr/bin/env python3

from sys import stdin as I

def solve(T):
  N = list(I.readline()[:-1])

  for i in range(len(N)-1, 0, -1):
    if N[i-1] > N[i]:
      N[i-1] = chr(ord(N[i-1]) - 1)
      N[i:] = ['9'] * (len(N) - i)

  N = int(''.join(N))
  print("Case #%i: %i" % (T, N))

T = int(I.readline())
for i in range(T):
  solve(i + 1)
