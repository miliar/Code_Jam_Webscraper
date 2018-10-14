#!/usr/bin/python
"""
Bathrooms
"""
import sys, os, math


def max_min(gap):
    if (gap == 1):
        return 0, 0
    if (gap == 2):
        return 1, 0
    if (gap == 3):
        return 1, 1
    if (gap % 2 == 0):
        return int(gap/ 2), int(gap/ 2) -1
    return int(gap / 2), int(gap / 2)


def best_gap(gaps):
    max_gap = max(gaps.keys(), key=int)
    return max_gap


def add_gap(gaps, gap):
    gaps[gap] = gaps.get(gap, 0) + 1


def rem_gap(gaps, max_gap):
    gaps[max_gap] = gaps[max_gap] -1
    if (gaps[max_gap] < 1):
        del gaps[max_gap]


def bathroom(num_stalls, people):
    gaps = dict()
    max_gap = num_stalls
    min_gap = num_stalls
    gaps[num_stalls] = 1
    for _ in range(0,people):
        used_gap = best_gap(gaps)
        rem_gap(gaps, used_gap)
        (max_gap, min_gap) = max_min(used_gap)
        add_gap(gaps, max_gap)
        add_gap(gaps, min_gap)
    return "{} {}".format(max_gap, min_gap)


def solve(a, b):
    """Returns a string result to one case of a problem"""
    return bathroom(a, b)


# Shared########################################################################
def main():
    with open(sys.argv[1], 'rU') as f_in:
        cases = int(f_in.readline().strip())
        for case in range(1, cases + 1):
            # Get input data
            a, b = [int(x) for x in f_in.readline().strip().split()]
            # a = f_in.readline().strip()
            # Solve and output
            print("Case #{}: {}".format(case, solve(a, b)))


if __name__ == '__main__':
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        main()
    elif len(sys.argv) > 1 and not os.path.exists(sys.argv[1]):
        print "File '" + str(sys.argv[1]) + "' does not exist!"
    else:
        print "No file supplied! Run program this way: '" + str(
            sys.argv[0]) + " something.in'"
