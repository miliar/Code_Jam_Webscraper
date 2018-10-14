#!/usr/bin/python3
T = int(input())
for t in range(1, T+1):
  [M, s] = input().split()
  M = int(M)
  s = [int(c) for c in s]
  already = 0
  add = 0
  for need in range(M + 1):
    if need > already:
      add += need - already
      already = s[need] + need
    else:
      already += s[need]
  print('Case #{}: {}'.format(t, add))

