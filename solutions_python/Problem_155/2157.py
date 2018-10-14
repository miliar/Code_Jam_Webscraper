#!/usr/bin/env python

from sys import stdin


def main():
    total_case_count = int(stdin.readline())
    for case_index in range(1, total_case_count + 1):
        input_data = stdin.readline().split(' ')
        shy_counts = [int(c) for c in input_data[1].strip()]
        solution = 0
        total_people = 0
        for shy_index, shy_value in enumerate(shy_counts):
            if total_people < shy_index:
                diff = shy_index - total_people
                total_people += diff
                solution += diff
            total_people += shy_value

        print 'Case #%s: %s' % (case_index, solution)


if __name__ == '__main__':
    main()
