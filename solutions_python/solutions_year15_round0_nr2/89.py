#!/usr/bin/env python3

def solve(D, plates):
  best = max(plates)
  for k in range(1, max(plates)):
    score = k + sum((p - 1) // k for p in plates)
    best = min(best, score)
  return best

def main():
  T = int(input())
  for case in range(1, T + 1):
    D = int(input())
    plates = list(map(int, input().split()))
    answer = solve(D, plates)
    print("Case #%d: %s" % (case, answer))

main()

