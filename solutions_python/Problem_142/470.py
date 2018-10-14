#!/usr/bin/env python3

import sys

def get_chars_counts(s):
  chars = [s[0]]
  counts = [1]
  for c in s[1:]:
    if c != chars[-1]:
      chars.append(c)
      counts.append(1)
    else:
      counts[-1] += 1
  return chars, counts

def solve():
  N = int(input())
  strings = [input().strip() for i in range(N)]
  chars, counts = dict(), dict()
  chars[0], counts[0] = get_chars_counts(strings[0])
  for i in range(1, N):
    chars[i], counts[i] = get_chars_counts(strings[i])
    if chars[i]  != chars[0]:
      return "Fegla Won"
  total = 0
  for j in range(len(chars[0])):
    mean = sum(counts[i][j] for i in range(N)) / N
    a = int(mean)
    b = a + 1
    cost_a = sum(abs(counts[i][j] - a) for i in range(N))
    cost_b = sum(abs(counts[i][j] - b) for i in range(N))
    cost = min(cost_a, cost_b)
    total += cost
  return total

def main():
  cases = int(input())
  for i in range(cases):
    solution = solve()
    print("Case #%d: %s" % (i + 1, solution))

if __name__ == "__main__":
  main()

