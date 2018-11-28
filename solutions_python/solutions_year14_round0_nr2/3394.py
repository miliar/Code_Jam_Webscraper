#!/usr/bin/env python3

"""
Google Code Jam 2014 - Qualification Round - 2. Problem
"""
__author__ = 'Luka Sterbic'

import sys


def calc_time_fixed_factories(c, f, x, n):
    rate = 2.0
    time = 0.0

    for factory in range(n):
        time += c / rate
        rate += f

    return time + x / rate


def calc_best_time(c, f, x):
    time = calc_time_fixed_factories(c, f, x, 0)
    factories = 1

    while True:
        new_time = calc_time_fixed_factories(c, f, x, factories)

        if new_time > time:
            break

        time = new_time
        factories *= 2

    min_factories = factories // 4
    max_factories = factories

    times = [calc_time_fixed_factories(c, f, x, n)
             for n in range(min_factories, max_factories + 1)]

    return min(times)



def main(path):
    with open(path) as file:
        test_cases = int(file.readline())

        for test in range(1, test_cases + 1):
            c, f, x = [float(num) for num in file.readline().split()]
            print("Case #%d: %0.7f" % (test, calc_best_time(c, f, x)))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 cookie_clicker_alpha.py input_file")
        sys.exit(1)

    main(sys.argv[1])