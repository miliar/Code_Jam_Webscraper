#!/usr/bin/env python3

import sys

def next_line():
    return sys.stdin.readline().strip()

def next_int():
    return int(next_line())

def next_row():
    return set(int(n) for n in next_line().split())

def get_output(sa, sb):
    r = sa & sb
    if not r:
        return 'Volunteer cheated!'
    if len(r) > 1:
        return 'Bad magician!'
    return list(r)[0]

def read_set():
    selection = next_int()
    rows = [next_row() for i in range(4)]
    return rows[selection - 1]

def run_test(i):
    sa = read_set()
    sb = read_set()
    return 'Case #{}: {}'.format(i + 1, get_output(sa, sb))

results = [run_test(i) for i in range(next_int())]
sys.stdout.write('\n'.join(results))
