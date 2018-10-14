#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin

def main():
  t = int(stdin.readline().strip())
  for i in range(t):
    [d, n] = list(map(int, stdin.readline().strip().split(' ')))
    positions = [list(map(int, stdin.readline().strip().split(' '))) for _ in range(n)]
    print("Case #{}: {:.6f}".format(i+1, solve(d, n, positions)))

def solve(d, n, positions):
  t = max([(d - k) / s for k, s in positions])
  return d / t

if __name__=="__main__":
  main()
