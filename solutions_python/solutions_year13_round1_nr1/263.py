#!/usr/bin/env python3

def feasible(r, t, n):
  return n * (2 * r + 1) + 2 * n * (n - 1) <= t

def solve(r, t):
  low = 1
  high = t
  while high - low > 1:
    mid = (high + low) // 2
    if feasible(r, t, mid):
      low = mid
    else:
      high = mid
  if feasible(r, t, high):
    return high
  else:
    return low

def main():
  T = int(input())
  for case in range(1, T + 1):
    r, t = map(int, input().split())
    print("Case #%d: %s" % (case, solve(r, t)))

if __name__ == "__main__":
  main()

