#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math, sys


def is_palindrome(number):
  str_number = str(number)
  return str_number == str_number[::-1]


def is_fair_and_square(number):
  if not is_palindrome(number):
    return False
  square_root = math.sqrt(number)
  return square_root.is_integer() and is_palindrome(int(square_root))


if __name__ == "__main__":
  input_filepath = sys.argv[1]

  with open(input_filepath, "rt") as input_file:
    T = int(next(input_file))

    for i in range(1, T + 1):
      range_start, range_end = map(int, next(input_file).split(" "))

      palindrome_count = 0
      for n in range(range_start, range_end + 1):
        if is_fair_and_square(n):
          palindrome_count += 1

      print("Case #%d: %d" % (i, palindrome_count))

    assert(i == T)
