#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin

def main():
  ts = int(stdin.readline())
  for idx in range(1, ts+1):
    nums = stdin.readline().split(" ")
    n, v, x = int(nums[0]), float(nums[1]), float(nums[2])
    xs = []
    for i in range(n):
      xs.append(list(map(float, stdin.readline().split(" "))))
    print("Case #%d: %s" % (idx, solve(n, v, x, xs)))

def solve(n, v, x, xs):
  if n == 1:
    [r, c] = xs[0]
    if c == x:
      return "%.7f" % (v / r)
    else:
      return "IMPOSSIBLE"
  else:
    [r1, c1], [r2, c2] = xs[0], xs[1]
    if (c1 < x and c2 < x) or (c2 > x and c1 > x):
      return "IMPOSSIBLE"
    elif c1 == c2 == x:
      return "%.7f" % (v / (r1+r2))
    else:
      t2 = (x*v-c1*v) / (r2*(c2-c1))
      t1 = (v-r2*t2) / r1
      return "%.7f" % max(t1, t2)

if __name__=="__main__":
   main()
