#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


DIMENSION = 4


def solve(first_answer, first_square, second_answer, second_square):
  choices1 = frozenset(first_square[first_answer - 1])
  choices2 = frozenset(second_square[second_answer - 1])
  union = choices1 & choices2
  if not union:
    return "Volunteer cheated!"
  if len(union) > 1:
    return "Bad magician!"
  assert(len(union) == 1)
  return next(iter(union))


if __name__ == "__main__":
  input_filepath = sys.argv[1]
  output_filepath = "output.txt"

  with open(input_filepath, "rt") as input_file:
    T = int(next(input_file))

    for i in range(1, T + 1):
      first_answer = int(next(input_file))
      first_square = tuple(tuple(map(int, next(input_file).split(" "))) for _ in range(DIMENSION))
      second_answer = int(next(input_file))
      second_square = tuple(tuple(map(int, next(input_file).split(" "))) for _ in range(DIMENSION))
      print("Case #%u: %s" % (i, solve(first_answer, first_square, second_answer, second_square)))

    assert(i == T)
