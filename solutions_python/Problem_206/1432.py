#! /usr/bin/env python3
import sys


def solve(d: int, h: list) -> float:

    max_t = 0

    for hi in h:
        time_i = float(d - hi['K']) / hi['S']
        max_t = max(max_t, time_i)

    return float(d) / max_t


def main():
    filename = sys.argv[1]
    f = open(filename, 'r')

    test = None
    test_i = 1

    for i, line in enumerate(f):

        # Skip test count line
        if i == 0:
            continue

        if test is None:
            d, n = line.split()
            test = {}
            test['D'] = int(d)
            test['N'] = int(n)
            test['H'] = []
            continue

        if test['N'] > len(test['H']):
            k, s = line.split()
            test['H'].append({'K': int(k), 'S': int(s)})

        if test['N'] != len(test['H']):
            continue

        # Run solver
        res = solve(test['D'], test['H'])

        # Format the output
        line = 'Case #{}: {}'.format(test_i, res)
        test_i += 1
        test = None

        # Print the output
        print(line)

if __name__ == '__main__':
    main()
