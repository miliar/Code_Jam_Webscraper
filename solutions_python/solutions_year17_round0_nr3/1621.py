#!/usr/bin/env python
"""Problem C. Bathroom Stalls"""

import heapq
import sys


def file_lines(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line


def main():
    if len(sys.argv) < 2:
        print('Usage: {:s} <input-file>'.format(sys.argv[0]))
        sys.exit(1)

    lines = file_lines(sys.argv[1])

    for i in range(int(next(lines))):
        print('Case #{:d}: '.format(i+1), end='')

        num_stalls, num_people = [int(x) for x in
                next(lines).strip().split(' ')]

        if num_people == num_stalls:
            print("0 0")
            continue

        # interval size is negative for sorting purposes
        # (interval_size, left_most_idx
        intervals = [(-num_stalls, 0)]

        for j in range(num_people):
            interval = heapq.heappop(intervals)
            start = interval[1]
            width = -interval[0]

            left_width = (width - 1) // 2
            right_width = width - left_width - 1

            if right_width > 0:
                heapq.heappush(intervals, (-right_width, start + left_width + 1))

            if left_width > 0:
                heapq.heappush(intervals, (-left_width, start))

        max_width = left_width if left_width > right_width else right_width
        min_width = left_width if left_width < right_width else right_width

        print("{:d} {:d}".format(max_width, min_width))


if __name__ == '__main__':
    main()
