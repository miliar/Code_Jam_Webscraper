#!/usr/bin/env python3

import sys

def solve():
  A, B, K = map(int, input().split())
  counter = 0
  for i in range(A):
    for j in range(B):
      if i & j < K:
        counter += 1
  return counter

def main():
  cases = int(input())
  for i in range(cases):
    solution = solve()
    print("Case #%d: %s" % (i + 1, solution))

if __name__ == "__main__":
  main()

