#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin

def main():
  t = int(stdin.readline().strip())
  for i in range(t):
    [n, k] = list(map(int, stdin.readline().strip().split(' ')))
    u = float(stdin.readline().strip())
    ps = list(map(float, stdin.readline().strip().split(' ')))
    print("Case #{}: {:.6f}".format(i+1, solve(n, k, u, ps)))

def prod(l):
  x = 1.0
  for y in l:
    x *= y
  return x

def solve(n, k, u, ps):
  if u >= n - sum(ps):
    return 1
  ps = sorted(ps)
  i = 0
  while u > 0.0:
    if i < n - 1 and ps[i] == ps[i+1]:
      i += 1
      continue
    dp = ps[i+1] - ps[i] if i < n - 1 else 1 - ps[i]
    all_dp = dp * (i+1)
    if u >= all_dp:
      u -= all_dp
      for j in range(i+1):
        ps[j] += dp
    else:
      for j in range(i+1):
        ps[j] += (u / (i+1))
      u = 0.0
    i += 1
    if i == n: break
  return prod(ps)

if __name__=="__main__":
  main()
