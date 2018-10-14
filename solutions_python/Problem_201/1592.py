# coding=utf-8

from __future__ import (absolute_import, division, generators, nested_scopes,
                        print_function, unicode_literals, with_statement)

from heapq import heappush, heappop
from math import floor

def stall(n, k):
  sizes = []
  size_to_count = {}

  def push(size, count):
    if size_to_count.has_key(size):
      size_to_count[size] += count
      # It's already in the heap
    else:
      heappush(sizes, -size)
      size_to_count[size] = count

  def pop():
    size = -heappop(sizes)
    return size, size_to_count.pop(size)

  push(n, 1)
  while k > 0:
    gap, count = pop()
    k -= count
    gap -= 1
    left_gap = int(floor(gap / 2))
    right_gap = gap - left_gap
    if left_gap > 0:
      push(left_gap, count)
    if right_gap > 0:
      push(right_gap, count)
  return '{} {}'.format(max(left_gap, right_gap), min(left_gap, right_gap))

if __name__ == '__main__':
  num_cases = int(raw_input())
  for case in range(num_cases):
    label = 'case #{}:'.format(case + 1)
    n, k = [int(x) for x in raw_input().split(' ')]
    occupied = stall(n, k)
    print(label, occupied)
