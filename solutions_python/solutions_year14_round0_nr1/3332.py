#!/usr/bin/bash

import sys

test_input = """3
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 5 4
3 11 6 15
9 10 7 12
13 14 8 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
"""

num_cases = int(sys.stdin.readline())
inp = sys.stdin.readlines()

def get_grid(inp):
  out = []
  for ii in range(0, 4):
    r = inp.pop(0)
    out.append(map(int, r.split(" ")))
  return out

cur_case = 0

while cur_case < num_cases:
  ans_1 = int(inp.pop(0)) - 1
  grid_a = get_grid(inp)
  used_rows = grid_a[ans_1]

  ans_2 = int(inp.pop(0)) - 1
  grid_b = get_grid(inp)
  used_cols = []
  for ii in range(0, 4):
    used_cols.append(grid_b[ans_2][ii])

  commons = set(used_rows).intersection(set(used_cols))
  if len(commons) == 0:
    status = "Volunteer cheated!"
  elif len(commons) == 1:
      status = list(commons)[0]
  else:
    status = "Bad magician!"

  print "Case #{}: {}".format(cur_case + 1, status)
  cur_case += 1

