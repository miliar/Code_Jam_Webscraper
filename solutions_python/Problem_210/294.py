#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin

def float_line():
  return list(map(float, stdin.readline().strip().split(' ')))

def main():
  t = int(stdin.readline().strip())
  for i in range(t):
    [ac, aj] = list(map(int, stdin.readline().strip().split(' ')))
    cs = [float_line() for _ in range(ac)]
    js = [float_line() for _ in range(aj)]
    print("Case #{}: {}".format(i+1, solve(ac, aj, cs, js)))

def solve(ac, aj, cs, js):
  if ac < 2 and aj < 2:
    return 2
  ds = cs if ac == 2 else js
  a = min(ds[0][0], ds[1][0])
  aa = max(ds[0][0], ds[1][0])
  b = max(ds[0][1], ds[1][1])
  bb = min(ds[0][1], ds[1][1])
  if b - a <= 720 or (bb + 1440 - aa) <= 720:
    return 2
  return 4

if __name__=="__main__":
  main()
