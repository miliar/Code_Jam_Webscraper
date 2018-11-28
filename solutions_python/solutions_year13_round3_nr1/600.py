#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools, itertools, string, sys


VOYELS = frozenset("aeiou")
CONSONANTS = frozenset(itertools.filterfalse(VOYELS.__contains__, string.ascii_lowercase))


def has_n_consecutive_consonants(word, n):
  consonants_in_a_row_count = 0
  for c in word:
    if c in VOYELS:
      consonants_in_a_row_count = 0
      continue
    consonants_in_a_row_count += 1
    if consonants_in_a_row_count == n:
      return True
  return False


def substrings(s):
  yield ""
  for start in range(len(s)):
    for end in range(start + 1, len(s) + 1):
      yield s[start:end]


if __name__ == "__main__":
  input_filepath = sys.argv[1]

  with open(input_filepath, "rt") as input_file:
    test_case_count = int(next(input_file))

    for i in range(1, test_case_count + 1):
      word, n = next(input_file).split(" ")
      n = int(n)
      sol = len(tuple(filter(None, map(functools.partial(has_n_consecutive_consonants, n=n), substrings(word)))))

      print("Case #%d: %d" % (i, sol))

    assert(i == test_case_count)
