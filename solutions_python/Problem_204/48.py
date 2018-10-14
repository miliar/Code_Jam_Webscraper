#!/usr/bin/env python3

def process(N, P, R, Q):
  arr = []
  for i, l in enumerate(Q):
    r = R[i]
    a = []
    for q in sorted(l):
      lo = -(-(q * 10) // (r * 11))
      hi = (q * 10) // (r * 9)
      if lo <= hi:
        a.append((lo, hi))
    arr.append(a)
  kits = 0
  while all(len(i) for i in arr):
    c = [i[0] for i in arr]
    m = max(t[0] for t in c)
    s = [t for t in range(N) if c[t][1] < m]
    if not s:
      kits += 1
      s = range(N)
    for t in s:
      arr[t] = arr[t][1:]
  return kits

T = int(input())
for case in range(1, T+1):
  N, P = map(int, input().split())
  R = list(map(int, input().split()))
  Q = [list(map(int, input().split())) for _ in range(N)]
  res = process(N, P, R, Q)
  print("Case #{}: {}".format(case, res))

