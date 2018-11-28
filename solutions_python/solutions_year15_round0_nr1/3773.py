#!/usr/bin/env python

import fileinput

def min_friends(persons):
    """Find minimum number of friends

    Each element of `people` gives the number of people in the
    audience with shyness level i, where i is the index of the
    element with 0 <= i < k, where k is the maximum shyness
    level.

    Find the minimum number of people needed to have everyone in
    the audience stand up.
    """
    count = 0
    friends = 0
    for i, p in enumerate(persons):
        m = 0
        if p > 0:
            m = max(i - count, 0)
        count += p + m
        friends += m
    

    return friends 

def solve(case):
    max_shyness = case[0]

    return min_friends(int(p) for p in list(case[1:].strip()))


if __name__ == "__main__":
    lines = fileinput.input()

    n_cases = int(lines.readline())

    for i, case in enumerate(lines):
        friends = solve(case)
        print("Case #{}: {}".format(i + 1, friends))


