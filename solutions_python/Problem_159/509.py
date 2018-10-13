#!/usr/bin/env python

import sys

def solve(numbers):
    min_sum = 0
    min_rate = 0
    for i, n in enumerate(numbers):
        if i == 0:
            continue
        diff = numbers[i - 1] - n
        if diff > 0:
            min_sum += diff
            min_rate = max(min_rate, diff)

    min_rate_sum = 0
    for i, n in enumerate(numbers[:-1]):
        min_rate_sum += min(min_rate, n)

    return (min_sum, min_rate_sum)


if __name__ == '__main__':
    input_file = open(sys.argv[1])
    T = int(input_file.readline().strip())

    for x in xrange(T):
        n = input_file.readline()
        input_numbers = [int(w) for w in input_file.readline().strip().split(' ')]
        y, z = solve(input_numbers)
        print "Case #{case}: {y} {z}".format(
            case=x+1,
            y=y,
            z=z
        )

