#!/usr/bin/env python

import sys

def solve_case(case_num):
    first_answer = int(sys.stdin.readline())
    rows_to_skip = 1

    while rows_to_skip < first_answer:
        skipped = sys.stdin.readline()
        rows_to_skip += 1

    first_row = sys.stdin.readline()
    first_row_numbers = set([x.strip() for x in first_row.split(' ')])

    while rows_to_skip < 4:
        skipped = sys.stdin.readline()
        rows_to_skip += 1

    second_answer = int(sys.stdin.readline())
    rows_to_skip = 1

    while rows_to_skip < second_answer:
        skipped = sys.stdin.readline()
        rows_to_skip += 1

    second_row = sys.stdin.readline()
    second_row_numbers = set([x.strip() for x in second_row.split(' ')])

    while rows_to_skip < 4:
        skipped = sys.stdin.readline()
        rows_to_skip += 1

    common_nums = list(second_row_numbers & first_row_numbers)

    if len(common_nums) == 0:
        print "Case #%s: Volunteer cheated!" % case_num
    elif len(common_nums) == 1:
        print "Case #%s: %s" % (case_num, common_nums[0])
    else:
        print "Case #%s: Bad magician!" % case_num

def main():
    test_cases = sys.stdin.readline()
    cases_solved = 0

    while cases_solved < test_cases:
        cases_solved += 1
        solve_case(cases_solved)

if __name__ == '__main__':
    main()
