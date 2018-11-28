#!/usr/bin/env python

import sys

case = int(sys.stdin.readline())

for i in range(case):
    first_answer = int(sys.stdin.readline())
    first_rows = []
    for j in range(4):
        row = sys.stdin.readline()
        first_rows.append(set([int(p) for p in row.split(' ')]))

    second_answer = int(sys.stdin.readline())
    second_rows = []
    for j in range(4):
        row = sys.stdin.readline()
        second_rows.append(set([int(p) for p in row.split(' ')]))

    common = first_rows[first_answer-1] & second_rows[second_answer-1]

    if len(common) == 0:
        print('Case #%d: Volunteer cheated!' % (i+1))
    elif len(common) == 1:
        print('Case #%d: %d' % (i+1, common.pop()))
    else:
        print('Case #%d: Bad magician!' % (i+1))
