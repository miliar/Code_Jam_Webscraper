#!/usr/bin/env python3

def solve(X, R, C):
  if (R * C) % X != 0:
    richard_wins = True
  elif X == 1 or X == 2:
    richard_wins = False
  elif X == 3:
    richard_wins = R == 1 or C == 1
  elif X == 4:
    richard_wins = R in {1, 2} or C in {1, 2}
  elif X >= 7:
    richard_wins = True
  if richard_wins:
    return "RICHARD"
  else:
    return "GABRIEL"

def main():
  T = int(input())
  for case in range(1, T + 1):
    X, R, C = map(int, input().split())
    answer = solve(X, R, C)
    print("Case #%d: %s" % (case, answer))

main()

