#!/usr/bin/env python3

import sys


def flip(s, from_idx, to_idx):
  return s[:from_idx] + "".join("+" if c == "-" else "-" for c in s[from_idx:to_idx + 1]) + s[to_idx + 1:]


def solve(S, K):
  count = 0
  s = S
  for i in reversed(range(len(S))):
    if s[i] == "-":
      if i >= K - 1:
        s = flip(s, i - K + 1, i)
        count += 1
      else:
        return "IMPOSSIBLE"
  return str(count)


if __name__ == "__main__":
  input_filepath = sys.argv[1]

  with open(input_filepath, "rt") as input_file:
    T = int(next(input_file))

    for i in range(1, T + 1):
      S, K = next(input_file).split(" ")
      K = int(K)
      print("Case #%u: %s" % (i, solve(S, K)))

    assert(i == T)
