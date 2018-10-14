#!/usr/bin/env python
from __future__ import print_function

import sys

INPUT_FILE = "a2.in"
OUTPUT_FILE = "a2.out"


def log(message):
    print(message, file=sys.stderr)

with open(INPUT_FILE, 'r') as fin, open(OUTPUT_FILE, 'w') as fout:
    sys.stdout = fout

    T = int(fin.readline())
    for tc in range(T):
        log('Test Case %d' % (tc+1))

        D, N = [int(i) for i in fin.readline().split()]

        total_time = 0.0
        for i in range(N):
            K, S = [int(i) for i in fin.readline().split()]
            time = float((D - K)) / float(S)
            if time > total_time:
                total_time = time

        res = float(D) / total_time

        print('Case #%d: %.6f' % (tc+1, res))
