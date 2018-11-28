#! /usr/bin/env python

from __future__ import print_function
from sys import stdin

N = int(stdin.readline())
for case in range(1, N+1):
    count, snaps = map(int, stdin.readline().split())
    needed = (1 << count) - 1
    print("Case #{0}:".format(case),
          "ON" if (snaps & needed == needed) else "OFF")
