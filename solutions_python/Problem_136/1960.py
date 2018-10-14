#!/usr/bin/env python3
import sys


def process_input(filename):
    with open(filename) as f:
        f.readline()

        while True:
            line = f.readline()

            if not line:
                break

            yield tuple(float(n) for n in line.split())


def solve(factory_cost, increment_factor, target_cookies):
    seconds_passed  = 0
    current_factor  = 2

    while True:
        remaining_time = seconds_passed + target_cookies / current_factor

        next_factory_time   = factory_cost / current_factor
        next_remaining_time = seconds_passed + next_factory_time + target_cookies / (current_factor + increment_factor)

        if next_remaining_time >= remaining_time:
            break

        seconds_passed += next_factory_time
        current_factor += increment_factor

    return round(remaining_time, 7)


if __name__ == '__main__':
    try:
        filename = sys.argv[1]
    except IndexError:
        print('Missing filename', file=sys.stderr)
        sys.exit(1)

    input_gen = process_input(filename)

    for case_num, (c, f, k) in enumerate(input_gen):
        print("Case #{}: {}".format(case_num+1, solve(c, f, k)))
