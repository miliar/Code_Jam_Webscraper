#! /usr/bin/python

import sys

def solve(C, F, X):
  cur_time = 0
  cur_cookies = 0
  cur_farms = 0

  while cur_cookies < X:
    time_to_nxt_farm = C / (2.0 + cur_farms * F)
    time_to_goal = (X-cur_cookies) / (2.0 + cur_farms * F)
    if time_to_goal < time_to_nxt_farm:
      return cur_time + time_to_goal

    cur_time += time_to_nxt_farm
    cur_cookies += (2.0 + cur_farms * F) * time_to_nxt_farm

    remaining_time_without_farm = (X-cur_cookies) / (2.0 + cur_farms * F)
    remaining_time_with_farm    = X / (2.0 + (cur_farms+1) * F)
    if remaining_time_with_farm < remaining_time_without_farm:
      cur_farms += 1
      cur_cookies = 0

  return cur_time 



fd = open(sys.argv[1])

num_cases = int(fd.readline())

for i in range(0, num_cases):
  (c, f, x) = [float(x) for x in fd.readline().strip().split(" ")]
  output = solve(c, f, x)
  print "Case #%d:" % (i+1), output

