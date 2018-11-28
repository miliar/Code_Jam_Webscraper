#!/usr/bin/env python3

import sys


def is_tidy(n):
  prev = -1
  for c in map(int, str(n)):
    if c < prev:
      return False
    prev = c
  return True


def solve(N):
  for n in range(N, -1, -1):
    if is_tidy(n):
      return n
  assert(False)


if __name__ == "__main__":
  input_filepath = sys.argv[1]

  with open(input_filepath, "rt") as input_file:
    T = int(next(input_file))

    for i in range(1, T + 1):
      N = int(next(input_file))
      print("Case #%u: %s" % (i, solve(N)))

    assert(i == T)
