# coding=utf-8

from __future__ import (absolute_import, division, generators, nested_scopes,
                        print_function, unicode_literals, with_statement)

num_cases = int(raw_input())
for case in range(num_cases):
  testcase = raw_input().split(' ')
  pancake = [x == '+' for x in testcase[0]]
  k = int(testcase[1])
  flips = 0
  for i in range(len(pancake) + 1 - k):
    if not pancake[i]:
      pancake[i:i+k] = [not x for x in pancake[i:i+k]]
      flips += 1
  all_flipped = all(pancake)
  label = 'case #{}:'.format(case + 1)
  if all_flipped:
    print(label, flips)
  else:
    print(label, 'IMPOSSIBLE')
