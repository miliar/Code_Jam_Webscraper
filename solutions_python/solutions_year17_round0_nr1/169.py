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

        S, K = fin.readline().split()
        S = list(S)
        K = int(K)

        res = 0
        for i in range(len(S)):
            if S[i] == '-':
                if K > len(S)-i:
                    res = "IMPOSSIBLE"
                    break
                else:
                    res += 1
                    for j in range(K):
                        S[i+j] = '+' if S[i+j] == '-' else '-'

        print('Case #%d: %s' % (tc+1, res))
