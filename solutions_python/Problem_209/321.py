#!/usr/bin/env python3

import sys
import math
from operator import itemgetter

def main():
  fi = sys.stdin
  fo = sys.stdout
  case_count = int(fi.readline().strip())
  for i in range(1, case_count+1):
    n, k, ps = read_input(fi)
    solution = solve(n, k, ps)
    display_and_clear(fo, i, solution)

def read_input(f):
  n, k = [int(arg) for arg in f.readline().split()]
  ps = []
  for i in range(n):
    p = [int(arg) for arg in f.readline().split()]
    ps.append(p)

  return n, k, ps

def display_and_clear(f, i, solution):
  f.write('Case #%d: %.6f\n' % (i, solution))
  f.flush()

def solve(n, k, ps):
  ps = sorted(ps, reverse=True)
  max_area = -float('inf')
  max_bottom = -1
  for i in range(n):
    area = max_given_bottom(n, k, ps, i)
    if area < max_area:
      continue
      #break
    else:
      max_area = area
      max_bottom = i

  return max_area

def max_given_bottom(n, k, ps, i):
  if (i + 1) + (k - 1) > n:
    return -float('inf')

  sides = []
  for r, h in ps[i+1:]:
    side = 2*math.pi*r*h
    sides.append(side)

  sides = sorted(sides, reverse=True)
  selections = sides[:k - 1]
  #print('top: %s' % ps[i])
  #print('remaining: %s' % selections)

  area = sum(selections)
  
  # bottom
  area += 2 * math.pi * ps[i][0] * ps[i][1]
  area += math.pi * (ps[i][0]**2)

  return area

if __name__ == '__main__':
  main()

