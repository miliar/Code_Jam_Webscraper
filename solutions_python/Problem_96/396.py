#!/usr/bin/env python
# coding: utf-8

import bisect

def solve(lst):
  N = lst[0]
  S = lst[1]
  P = lst[2]
  T = lst[3:]
  L = len(T)
  del lst

  ret = 0
  T.sort()
  at = bisect.bisect_left(T, P*3-2)
  ret += L - at
  T = T[:at]
  L = len(T)
  at = bisect.bisect_left(T, max(1, P*3-4))
  ret += min(S, L - at)
  return ret

for case in range(int(input())):
  print("Case #{0}: {1}".format(case+1, solve(list(map(int, input().split())))))
