#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def time_to_end(cookie_count, rate, win_count):
  return (win_count - cookie_count) / rate


def solve(C, F, X):
  time_enlapsed = 0
  cookie_count = 0
  rate = 2
  while cookie_count < X:
    if C >= X:
      # farm more expensive than win count => end
      time_enlapsed += time_to_end(cookie_count, rate, X)
      cookie_count = X
    elif cookie_count < C:
      # can not buy farm
      assert(cookie_count == 0)
      time_to_buy_farm = C / rate
      time_enlapsed += time_to_buy_farm
      cookie_count = C
    else:
      assert(cookie_count == C)
      # can buy farm, it it worth it?
      new_farm_cookie_rate = rate + F
      if time_to_end(cookie_count, rate, X) < time_to_end(0, new_farm_cookie_rate, X):
        # no => end
        time_enlapsed += time_to_end(cookie_count, rate, X)
        cookie_count = X
      else:
        # yes => buy farm
        cookie_count = 0
        rate = new_farm_cookie_rate
  assert(cookie_count == X)
  return time_enlapsed


if __name__ == "__main__":
  input_filepath = sys.argv[1]
  output_filepath = "output.txt"

  with open(input_filepath, "rt") as input_file:
    T = int(next(input_file))

    for i in range(1, T + 1):
      C, F, X = tuple(map(float, next(input_file).split(" ")))
      print("Case #%u: %.7f" % (i, solve(C, F, X)))

    assert(i == T)
