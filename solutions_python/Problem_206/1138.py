# coding=utf-8

from __future__ import (absolute_import, division, generators, nested_scopes,
                        print_function, unicode_literals, with_statement)

from math import ceil, floor

def horse(distance, pos_speeds):
  finish_times = [(distance - pos) / speed for pos, speed in pos_speeds]
  our_speed = distance / max(finish_times)
  return "%0.6f" % our_speed
  
if __name__ == '__main__':
  num_cases = int(raw_input())
  for case in range(num_cases):
    label = 'case #{}:'.format(case + 1)
    distance, horses = [int(x) for x in raw_input().split(' ')]
    pos_speeds = [[float(x) for x in raw_input().split(' ')] for i in range(horses)]
    print(label, horse(distance, pos_speeds))
