#!/usr/bin/env python
from __future__ import print_function

import sys

INPUT_FILE = "c3.in"
OUTPUT_FILE = "c3.out"


def log(message):
    print(message, file=sys.stderr)

with open(INPUT_FILE, 'r') as fin, open(OUTPUT_FILE, 'w') as fout:
    sys.stdout = fout

    T = int(fin.readline())
    for tc in range(T):
        log('Test Case %d' % (tc+1))

        N, K = [int(i) for i in fin.readline().split()]
        free_zones = {
            N: 1
        }
        while K > 0:
            size = max(free_zones.keys())
            zone_count = free_zones[size]
            del free_zones[size]
            size -= 1
            l = size / 2
            r = size - l
            if l not in free_zones:
                free_zones[l] = 0
            if r not in free_zones:
                free_zones[r] = 0
            free_zones[l] += zone_count
            free_zones[r] += zone_count
            K -= zone_count

        res = '%d %d' % (r, l)

        print('Case #%d: %s' % (tc+1, res))
