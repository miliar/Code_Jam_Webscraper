#!/usr/bin/python3

from fractions import gcd
from functools import reduce

t = int(input())

for c in range(1, t + 1):
  r, k, n = input().split(' ')
  r, k, n = int(r), int(k), int(n)
  a = input().split(' ')
  a = [int(q) for q in a + a]
  k1 = []
  k2 = []

  for i in range(n):
    b1 = 0
    b2 = 0
    for j in range(n):
      if b2 + a[i + j] > k:
        break
      b1 += 1
      b2 += a[i + j]
    k1.append(b1)
    k2.append(b2)

  now = 0
  bol = [False] * n
  bol1 = [0] * n
  bol2 = [0] * n
  stp = 0
  inc = 0

  while r > 0 and not bol[now]:
    bol[now] = True
    bol1[now] = stp
    bol2[now] = inc

    stp += 1
    inc += k2[now]
    now = (now + k1[now]) % n
    r -= 1

  if r > 0:
    mul = r // (stp - bol1[now])
    inc += mul * (inc - bol2[now])
    r %= stp - bol1[now]

  while r > 0:
    inc += k2[now]
    now = (now + k1[now]) % n
    r -= 1

  print('Case #%d: %s' % (c, inc))
  
