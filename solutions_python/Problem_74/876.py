#!/usr/bin/python

import sys

# Activestate Recipe 439095
def group(it, n):
  itr = iter(it)

  while True:
    yield tuple([itr.next() for i in range(n)])

def solve(line):
  l = line.split()
  l.pop(0)

  o_pos = 1
  o_last_time = 0
  b_pos = 1
  b_last_time = 0
  total_time = 0

  for (c, p) in group(l, 2):
    if c == 'O':
      time = abs(int(p) - o_pos)
      if time <= b_last_time:
        time = 0
        b_last_time = 0
      total_time += time - b_last_time + 1
      o_last_time += time - b_last_time + 1
      b_last_time = 0
      o_pos = int(p)
    elif c == 'B':
      time = abs(int(p) - b_pos)
      if time <= o_last_time:
        time = 0
        o_last_time = 0
      total_time += time - o_last_time + 1
      b_last_time += time - o_last_time + 1
      o_last_time = 0
      b_pos = int(p)

  return total_time

def main(filename):
  f = open(filename, "r")

  T = f.readline()

  case = 1
  for line in f:
    print "Case #" + str(case) + ":",

    print str(solve(line))

    case += 1

if __name__ == "__main__":
  main(sys.argv[1])
