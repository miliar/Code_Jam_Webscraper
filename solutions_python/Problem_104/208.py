#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on May 5, 2012

@author: daniel
'''
from Solver import Solver
from itertools import combinations
from collections import defaultdict

result = "\n%s\n%s"

class Sums(Solver):
  def solve(self, case):
    ints, *nums = map(int, self.fhi.readline().split())

    sums = defaultdict(list)

    for i in range(1, ints + 1):
      combos = combinations(nums, i)
      for combo in combos:
        s = sum(combo)

        sums[s].append(combo)
        if len(sums[s]) == 2 and not (set(sums[s][0]) & set(sums[s][1])):
          s0 = ' '.join(map(str, sums[s][0]))
          s1 = ' '.join(map(str, sums[s][1]))
          self.output(case, result % (s0, s1))

          return

if __name__ == '__main__':
    Sums(r'data/c_small.txt', r'data/c_small_out.txt')
