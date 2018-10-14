#!/usr/bin/env python3

import sys

r = len(bin(10 ** 12)) + 1

def rank(n):
  for i in range(r, -1, -1):
    if ((1 << i) & n):
      return i
  assert False

def is_pow2(q, p):
  while q > 0:
    if q % 2:
      return (p % q == 0)
    q = q // 2
  assert False

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def solve():
  P, Q = map(int, input().strip().split("/"))
  R = gcd(P, Q)
  P, Q = P // R, Q // R
  if not is_pow2(Q, P):
    return "impossible"
  return rank(Q) - rank(P)

def main():
  cases = int(input())
  for i in range(cases):
    solution = solve()
    print("Case #%d: %s" % (i + 1, solution))

if __name__ == "__main__":
  main()

