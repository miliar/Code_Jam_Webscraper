#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


LIMITS = (1, 100)


def is_possible_pattern(matrix):
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):

      val = matrix[i][j]
      if not (LIMITS[0] <= val <= LIMITS[1]):
        return False

      has_higher_in_row, has_higher_in_column = True, True

      try:
        next(filter(val.__lt__, matrix[i]))
      except StopIteration:
        has_higher_in_row = False

      try:
        column = tuple(matrix[x][j] for x in range(len(matrix)))
        next(filter(val.__lt__, column))
      except StopIteration:
        has_higher_in_column = False

      if has_higher_in_row and has_higher_in_column:
        return False

  return True


if __name__ == "__main__":
  input_filepath = sys.argv[1]
  output_filepath = "output.txt"

  with open(input_filepath, "rt") as input_file:
    T = int(next(input_file))

    for i in range(1, T + 1):
      N, M = map(int, next(input_file).split(" "))
      matrix = tuple(tuple(map(int, next(input_file).split(" "))) for n in range(N))

      possible = is_possible_pattern(matrix)

      print("Case #%d: %s" % (i, "YES" if possible else "NO"))

    assert(i == T)
