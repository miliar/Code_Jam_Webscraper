#!/usr/bin/env python3

def solve(A, N, motes):
  motes.sort()
  if A == 1:
    return len(list(filter(lambda mote: mote > 0, motes)))
  best = N
  moves_needed = 0
  for i in range(N):
    while A <= motes[i]:
      A += A - 1
      moves_needed += 1
    A += motes[i]
    best = min(best, moves_needed + (N - i - 1))
  return best

def main():
  T = int(input())
  for case in range(1, T + 1):
    A, N = map(int, input().split())
    motes = list(map(int, input().split()))
    print("Case #%d: %s" % (case, solve(A, N, motes)))

if __name__ == "__main__":
  main()

