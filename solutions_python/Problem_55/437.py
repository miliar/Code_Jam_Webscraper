#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Dmytro Molkov on 2010-05-07.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

import sys
import os


def main():
  data = open("/tmp/data")
  out = open("/tmp/out.data", "w")
  tests = int(data.readline())
  result = 0
  for i in range(1, tests + 1):
    splits = data.readline().split(" ")
    groups = data.readline().split(" ")
    rides = int(splits[0])
    capacity = int(splits[1])
    group_count = int(splits[2])
    index = 0
    result = 0
    for j in range(0, rides):
      current_capacity = capacity
      riders = 0
      while current_capacity + 1 >  int(groups[index]) and riders < group_count:
        result += int(groups[index])
        current_capacity -= int(groups[index])
        index = (index + 1) % group_count
        riders += 1
    out.write("Case #" + str(i) + ": " + str(result) + "\n")

if __name__ == '__main__':
  main()

