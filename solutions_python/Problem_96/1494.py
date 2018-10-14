#!/usr/bin/env python2.6
from __future__ import absolute_import, division, print_function

def solve_case(n, surprises, p, *totals):
    count = 0
    upper_limit = 3*p-2
    lower_limit = max(upper_limit - 3, 0)
    for total in totals:
        if total >= upper_limit:
            count += 1
        elif surprises and total > lower_limit:
            count += 1
            surprises -= 1
    return count

if __name__ == "__main__":
    T = int(raw_input())
    for i in range(1, T+1):
        print("Case #%d:" % i, solve_case(*(int(x) for x in raw_input().split())))
