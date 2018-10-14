#!/usr/bin/env python3

def solve(E, R, N, activities):
  d = dict()
  def solve(energy, i):
    if (energy, i) not in d:
      if i == len(activities):
        ans = 0
      else:
        ans = max(activities[i] * j + solve(min(energy - j +  R, E), i + 1) for j in range(energy + 1))
      d[energy, i] = ans
    return d[energy, i]
  return solve(E, 0)

def main():
  T = int(input())
  for case in range(1, T + 1):
    E, R, N = map(int, input().split())
    activities = list(map(int, input().split()))
    print("Case #%d: %s" % (case, solve(E, R, N, activities)))

if __name__ == "__main__":
  main()

