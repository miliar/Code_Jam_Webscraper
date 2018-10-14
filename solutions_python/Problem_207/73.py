#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin

def main():
  t = int(stdin.readline().strip())
  for i in range(t):
    [N, R, O, Y, G, B, V] = list(map(int, stdin.readline().strip().split(' ')))
    print("Case #{}: {}".format(i+1, solve(N, R, O, Y, G, B, V)))

def solve(N, R, O, Y, G, B, V):
  [c0, c1, c2] = sorted([(R, 'R'), (Y, 'Y'), (B, 'B')], reverse=True)
  p = c0[0]
  r = c1[0] + c2[0]
  if p > r:
    return "IMPOSSIBLE"
  k = r - p
  s1 = "{}{}{}".format(c0[1], c1[1], c2[1])
  s2 = "{}{}".format(c0[1], c1[1])
  s3 = "{}{}".format(c0[1], c2[1])
  return s1 * k + s2 * (c1[0] - k) + s3 * (c2[0] - k)

if __name__=="__main__":
  main()
