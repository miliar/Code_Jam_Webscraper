#! /usr/bin/python

import os, sys

T = int(sys.stdin.readline())

# For each test case
for t in range(1, T+1):
    first_grid = [None, None, None, None]
    second_grid = [None, None, None, None]
    first_ans = int(sys.stdin.readline()) - 1
    for i in range(0,4):
        first_grid[i] = [int(x) for x in sys.stdin.readline().split(' ')]
    second_ans = int(sys.stdin.readline()) - 1
    for i in range(0,4):
        second_grid[i] = [int(x) for x in sys.stdin.readline().split(' ')]
    res = [x for x in first_grid[first_ans] if x in second_grid[second_ans]]
    #
    if len(res) == 0:
        res_print = 'Volunteer cheated!'
    elif len(res) > 1:
        res_print = 'Bad magician!'
    else:
        res_print = res[0]
    #
    sys.stdout.write('Case #%s: %s\n' % (t, res_print))
