#!/usr/bin/env python3

from sys import stdin, stdout, stderr

def solve(N, mushrooms):
  method1 = 0
  for i in range(N - 1):
    method1 += max(mushrooms[i] - mushrooms[i + 1], 0)
  m = max(max(mushrooms[i] - mushrooms[i + 1], 0) for i in range(N - 1))
  method2 = 0
  for i in range(N - 1):
    method2 += min(mushrooms[i], m)
  return "%d %d" % (method1, method2)

def main():
  T = int(input())
  for case in range(1, T + 1):
    N = int(input())
    mushrooms = list(map(int, input().split()))
    answer = solve(N, mushrooms)
    print("Case #%d: %s" % (case, answer))

main()

