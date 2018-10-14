#!/usr/bin/env python3

import sys
from collections import Counter

def split_range(range_size):
    return (range_size // 2, (range_size - 1) // 2)

def next_arrival_outcome(empty_ranges):
    return split_range(max(empty_ranges.keys()))

def handle_arrivals(empty_ranges, num_arrivals):
    #for k in sorted(empty_ranges.keys()):
    #    print(k, empty_ranges[k])
    #print(num_arrivals)
    #print('---')

    big_range = max(empty_ranges.keys())
    num_ranges = empty_ranges[big_range]

    arrivals_handled = num_ranges
    if num_ranges > num_arrivals:
        arrivals_handled = num_arrivals
        empty_ranges[big_range] -= arrivals_handled
    else:
        del empty_ranges[big_range]

    L, R = split_range(big_range);
    empty_ranges[L] += arrivals_handled
    empty_ranges[R] += arrivals_handled
    return num_arrivals - arrivals_handled

def solve_case(n, num_people):
    empty_ranges = Counter()
    empty_ranges[n] = 1
    num_people -= 1
    while num_people > 0:
        num_people = handle_arrivals(empty_ranges, num_people)
    return next_arrival_outcome(empty_ranges)

def run_cases():
    next(sys.stdin)
    for i, line in enumerate(sys.stdin):
        n, k = line.strip().split()
        answer = solve_case(int(n), int(k));
        print('Case #{}: {} {}'.format(i+1, answer[0], answer[1]))

if __name__ == '__main__':
    run_cases()

