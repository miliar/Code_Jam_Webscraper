#!/usr/bin/env python3
# Copyright (C) 2015 Mansour Behabadi <mansour@oxplot.com>

from itertools import count

def run_test(aud_def):
  standing_count, extra_count = 0, 0
  for shyness_level, aud_count in zip(count(), map(int, aud_def)):
    if aud_count == 0:
      continue
    if standing_count < shyness_level:
      extra_needed = shyness_level - standing_count
      standing_count += extra_needed
      extra_count += extra_needed
    standing_count += aud_count
  return extra_count

def main():
  test_count = int(input())
  for ti in range(test_count):
    extra_count = run_test(input().split()[1])
    print('Case #%d: %d' % (ti + 1, extra_count))

if __name__ == '__main__':
  main()
