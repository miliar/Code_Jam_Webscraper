#!/usr/bin/env pypy

import sys,os

num_cases = int(sys.stdin.readline().strip())

for case in xrange(0,num_cases):
  pancakes, flipper_size = sys.stdin.readline().strip().split()
  pancakes = [c for c in pancakes]
  flipper_size = int(flipper_size)

  cur_neg = -1
  count = 0
  find_neg = -1
  if '-' in pancakes:
    find_neg = pancakes.index('-')
  while find_neg > cur_neg:
    if len(pancakes) - find_neg < flipper_size:
      break
    count += 1
    for i in range(find_neg, find_neg+flipper_size):
      if pancakes[i] == '+':
        pancakes[i] = '-'
      else:
        pancakes[i] = '+'
    cur_neg = find_neg
    if '-' in pancakes:
      find_neg = pancakes.index('-')
    else:
      find_neg = -1

  sys.stdout.write("Case #{}: {}\n".format(case+1, "IMPOSSIBLE" if find_neg != -1 else count))
