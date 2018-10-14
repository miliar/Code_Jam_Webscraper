#! /usr/bin/env python

import os
import sys


def get_input():
    file_name = sys.argv[1]

    test_cases = 0
    test_cases_data = []

    with open(os.path.abspath(file_name), 'r') as f:
        first_line = True
        one_field = 0

        field = []

        for line in f.readlines():
            line = line.replace('\n', '')

            if first_line:
                test_cases = int(line)
                first_line = False
                continue

            if not line:
                continue

            if one_field < 3:
                field.append(
                    [c for c in line]
                )
                one_field += 1
            elif one_field == 3:
                field.append(
                    [c for c in line]
                )
                test_cases_data.append(field)
                field = []
                one_field = 0
                continue

    return test_cases, test_cases_data


def process_field(field):
    for i in xrange(4):
        row_set = set(field[i])
        if len(row_set) == 1:
            player = row_set.pop()
            if player != '.':
                return '{0} won'.format(player)
        if len(row_set) == 2 and 'T' in row_set:
            player = row_set.pop()
            if player == 'T':
                player = row_set.pop()
            if player != '.':
                return '{0} won'.format(player)
    for j in xrange(4):
        col_set = set(
            [
                field[0][j],
                field[1][j],
                field[2][j],
                field[3][j],
            ]
        )
        if len(col_set) == 1:
            player = col_set.pop()
            if player != '.':
                return '{0} won'.format(player)
        if len(col_set) == 2 and 'T' in col_set:
            player = col_set.pop()
            if player == 'T':
                player = col_set.pop()
            if player != '.':
                return '{0} won'.format(player)
    left_diag_set = {
        field[i][i] for i in xrange(4)
    }
    if len(left_diag_set) == 1:
        player = left_diag_set.pop()
        if player != '.':
            return '{0} won'.format(player)
    if len(left_diag_set) == 2 and 'T' in left_diag_set:
        player = left_diag_set.pop()
        if player == 'T':
            player = left_diag_set.pop()
        if player != '.':
            return '{0} won'.format(player)
    right_diag_set = {
        field[i][3-i] for i in xrange(4)
    }
    if len(right_diag_set) == 1:
        player = right_diag_set.pop()
        if player != '.':
            return '{0} won'.format(player)
    if len(right_diag_set) == 2 and 'T' in right_diag_set:
        player = right_diag_set.pop()
        if player == 'T':
            player = right_diag_set.pop()
        if player != '.':
            return '{0} won'.format(player)

    has_dots = False
    for i in xrange(4):
        if '.' in field[i]:
            has_dots = True
            break

    if has_dots:
        return 'Game has not completed'
    else:
        return 'Draw'


def main():
    test_cases, test_cases_data = get_input()
    data = ''
    for test_case in xrange(test_cases):
        data += 'Case #{0}: {1}\n'.format(
            test_case + 1,
            process_field(test_cases_data[test_case])
        )
    print data
    with open(os.path.abspath('./data/output_a'), 'w') as f:
        f.write(data)


if __name__ == '__main__':
    main()