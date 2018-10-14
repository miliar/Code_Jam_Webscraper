#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def debug(a): sys.stderr.write(str(a) + '\n')
def readarray(foo): return [foo(e) for e in input().split()]
def readint(): return int(input().strip())

# debut = lambda x: None

T = readint()
for i in range(T):
    before_rownum = readint()
    before_row = []
    for j in [0, 1, 2, 3]:
        before_row.append(readarray(int))

    after_rownum = readint()
    after_row = []
    for j in [0, 1, 2, 3]:
        after_row.append(readarray(int))

    inter = set(before_row[before_rownum - 1]) & set(after_row[after_rownum - 1])
    if len(inter) == 0:
        message = 'Volunteer cheated!'
    elif len(inter) == 1:
        message = str(list(inter)[0])
    else:
        message = 'Bad magician!'
    print('Case #{0}: {1}'.format(i + 1, message))
