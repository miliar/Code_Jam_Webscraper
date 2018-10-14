#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


TEST = 1


def test():
  global TEST
  print('Case #%d:' % TEST, end=' ')
  TEST += 1
  N, K = map(int, input().split())
  i = 0
  d = {N: 1}
  l, r = N, N
  while i < K:
    v = max(d.keys())
    c = d[v]
    l, r = v // 2, (v - 1) // 2
    del d[v]
    if l not in d: d[l] = 0
    if r not in d: d[r] = 0
    d[l] += c
    d[r] += c
    i += c
  print(l, r)
  

T = int(input())
for _ in range(T): test()
