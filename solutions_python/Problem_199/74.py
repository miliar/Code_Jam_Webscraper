#!/usr/bin/env python3

def process(S, K):
  N = len(S)
  flips = 0
  sad = {i for i in range(N) if S[i] == '-'}
  while sad:
    t = min(sad)
    if t >= N: return 'IMPOSSIBLE'
    sad ^= set(range(t, t+K))
    flips += 1
  return flips

T = int(input())
for case in range(1, T+1):
  S, K = input().split()
  res = process(S, int(K))
  print("Case #{}: {}".format(case, res))

