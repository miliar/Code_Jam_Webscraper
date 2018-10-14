#!/usr/bin/env python
from __future__ import print_function

import sys

INPUT_FILE = "b1.in"
OUTPUT_FILE = "b1.out"


def log(message):
    print(message, file=sys.stderr)

with open(INPUT_FILE, 'r') as fin, open(OUTPUT_FILE, 'w') as fout:
    sys.stdout = fout

    T = int(fin.readline())
    for tc in range(T):
        log('Test Case %d' % (tc+1))

        N, R, O, Y, G, B, V = [int(i) for i in fin.readline().split()]

        if B > R+Y or R > B+Y or Y > B+R:
            res = 'IMPOSSIBLE'
        else:
            res = ''
            prev = ''
            start = ''
            while N > 0:
                if R == B and R == Y:
                    if start == 'R':
                        if prev == 'B':
                            prev = 'YRB'
                        else:
                            prev = 'BRY'
                    elif start == 'Y':
                        if prev == 'B':
                            prev = 'RYB'
                        else:
                            prev = 'BYR'
                    else:
                        if prev == 'Y':
                            prev = 'RBY'
                        else:
                            prev = 'YBR'

                    N -= 2
                    B -= 1
                    R -= 1
                    Y -= 1
                else:
                    if prev == '':
                        if R >= Y and R >= B:
                            prev = 'R'
                            R -= 1
                        elif B >= Y:
                            prev = 'B'
                            B -= 1
                        else:
                            prev = 'Y'
                            Y -= 1
                        start = prev
                    elif prev == 'R' and B >= Y and B > 0:
                        prev = 'B'
                        B -= 1
                    elif prev == 'R' and Y > 0:
                        prev = 'Y'
                        Y -= 1
                    elif prev == 'B' and R >= Y and R > 0:
                        prev = 'R'
                        R -= 1
                    elif prev == 'B' and Y > 0:
                        prev = 'Y'
                        Y -= 1
                    elif prev == 'Y' and R >= B and R > 0:
                        prev = 'R'
                        R -= 1
                    elif prev == 'Y' and B > 0:
                        prev = 'B'
                        B -= 1
                    else:
                        continue

                if len(res) > 0 and prev == res[-1]:
                    continue

                res += prev
                N -= 1

        print('Case #%d: %s' % (tc+1, res))
