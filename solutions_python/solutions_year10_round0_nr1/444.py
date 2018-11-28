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
  for i in range(1, tests + 1):
    splits = data.readline().split(" ")
    bytes = int(splits[0])
    clicks = int(splits[1])
    number = 2 ** bytes
    if (clicks + 1) % number == 0:
      out.write("Case #" + str(i) + ": ON\n")
    else:
      out.write("Case #" + str(i) + ": OFF\n")


if __name__ == '__main__':
  main()

