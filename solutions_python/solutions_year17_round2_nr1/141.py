#!/usr/bin/env python3
# input() reads a string with a line of input, stripping the '\n' (newline) at
# the end. This is all you need for most Google Code Jam problems.

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  d, n = [int(s) for s in input().split(" ")]
  soonest_arrival_time = 0
  for j in range(1, n + 1):
      k, s = [int(s) for s in input().split(" ")]
      arrival_time = (d - k) / s
      if arrival_time > soonest_arrival_time:
          soonest_arrival_time = arrival_time
  print("Case #{}: {}".format(i, d / soonest_arrival_time))
  # check out .format's specification for more formatting options
