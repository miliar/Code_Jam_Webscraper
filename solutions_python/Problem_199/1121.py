#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Uses https://github.com/rkistner/contest-algorithms

from __future__ import print_function
import sys
# from Set import Set

def debug(*args):
    print(*args, file=sys.stderr)

fin = sys.stdin
T = int(fin.readline())
for case in range(1, T + 1):
    s, ks = fin.readline().split()
    k = int(ks)
    debug(k, s)

    flipped = False
    flips = 0
    impossible = False
    queue = set()
    for i, c in enumerate(s):
        if i in queue:
            queue.remove(i)
            flipped = not flipped
        if (c == '-') ^ flipped:
            if i + k > len(s):
                impossible = True
            flipped = not flipped
            queue.add(i + k)
            flips += 1



    if impossible:
        print("Case #%d: %s" % (case, 'IMPOSSIBLE'))
    else:
        print("Case #%d: %s" % (case, flips))

