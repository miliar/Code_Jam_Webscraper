#! /usr/bin/env python

import os
import sys


def get_input():
    test_cases_data = {}

    with open(os.path.abspath(sys.argv[1]), 'r') as input_file:
        test_cases = int(input_file.readline())
        for i in xrange(test_cases):
            sizes = map(int, input_file.readline().split(' '))
            test_cases_data.setdefault(i, {})['sizes'] = sizes
            for j in xrange(sizes[0]):
                row = map(int, input_file.readline().split(' '))
                for value in row:
                    test_cases_data.setdefault(i, {}).setdefault(
                        'heights', set()
                    ).add(value)
                test_cases_data.setdefault(i, {}).setdefault(
                    'data', []
                ).append(row)

    return test_cases, test_cases_data


def process_data(data):
    heights = sorted(data.get('heights'), reverse=True)[1:]
    field = data.get('data')

    for height in heights:
        for i in xrange(len(field)):
            for j in xrange(len(field[i])):
                if field[i][j] == height:
                    ok_height_u, \
                        ok_height_d, \
                        ok_height_l, \
                        ok_height_r = (True, ) * 4
                    for k in xrange(i):
                        if field[k][j] > height:
                            ok_height_u = False
                            break
                    for k in xrange(len(field) - i):
                        if field[i + k][j] > height:
                            ok_height_d = False
                            break
                    for k in xrange(j):
                        if field[i][k] > height:
                            ok_height_l = False
                            break
                    for k in xrange(len(field[i]) - j):
                        if field[i][j + k] > height:
                            ok_height_r = False
                            break
                    if not ((ok_height_u and ok_height_d) or (ok_height_l and ok_height_r)):
                        return 'NO'
    return 'YES'


def main():
    test_cases, test_cases_data = get_input()

    data = ''

    for i in xrange(test_cases):
        result = process_data(test_cases_data.get(i))
        print result
        data += 'Case #{0}: {1}\n'.format(
            i + 1,
            result,
        )

    with open(os.path.abspath('./data/output_b'), 'w') as output:
        output.write(data)


if __name__ == '__main__':
    main()