#!/usr/bin/env python3

import functools

def nearest_left_dist(stalls, x):
  if stalls[x]: return 0
  i = 0
  while not stalls[x-i-1]:
    i += 1
  return i

def nearest_right_dist(stalls, x):
  if stalls[x]: return 0
  i = 0
  while not stalls[x+i+1]:
    i += 1
  return i

def choose_stall(stalls):
  N = len(stalls)
  L_s = [abs(nearest_left_dist(stalls, x)) for x in range(1,N-1)]
  R_s = [abs(nearest_right_dist(stalls, x)) for x in range(1,N-1)]
  sort_key = lambda i:(-min(L_s[i-1], R_s[i-1]), -max(L_s[i-1], R_s[i-1]), i)
  best = min((i for i in range(1,N-1) if not stalls[i]), key=sort_key)
  return (best, (min(L_s[best-1], R_s[best-1]), max(L_s[best-1], R_s[best-1])))

def fill_stalls(N, K):
  if N == K:
    return (0, 0)
  stalls = [1]+[0]*N+[1]
  sort_key = lambda i:(-min(L_s[i], R_s[i]), -max(L_s[i], R_s[i]), i)
  L_s = [0]+[abs(nearest_left_dist(stalls, x)) for x in range(1,N+1)]+[0]
  R_s = [0]+[abs(nearest_right_dist(stalls, x)) for x in range(1,N+1)]+[0]
  for j in range(K):
    best = min((i for i in range(1,N+1) if not stalls[i]), key=sort_key)
    stalls[best] = 1
    for x in range(1, N+1):
      if not stalls[x]:
        if best < x:
          L_s[x] = min(L_s[x], abs(x-best)-1)
        elif best > x:
          R_s[x] = min(R_s[x], abs(x-best)-1)
  return sorted((L_s[best], R_s[best]), reverse=True)

T = int(input())
for i in range(1, T+1):
  N, K = map(int, input().split())
  print("Case #{}: {}".format(i, ' '.join(map(str, fill_stalls(N, K)))))