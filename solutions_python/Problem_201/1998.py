#!/usr/bin/env python
import argparse
import itertools
import math


def min_max(stalls, i):
    l_s = list(reversed(stalls[:i])).index(1)
    r_s = stalls[i+1:].index(1)
    return min(l_s, r_s), max(l_s, r_s)


def choose(stalls):
    vals = []
    ultimate_min = 0
    for i, stall in enumerate(stalls):
        if stall == 0:
            minimum, maximum = min_max(stalls, i)
            if minimum >= ultimate_min:
                ultimate_min = minimum
                vals.append({
                    'index': i,
                    'minimum': minimum,
                    'maximum': maximum,
                })
    vals = sorted(vals, key=lambda v: (-v['minimum'], -v['maximum'], v['index']))
    return vals[0]


def choose2(stalls):
    run, index = longest_run(stalls)
    minimum, maximum = min_max_from_run(run)
    index = index + minimum
    return index, minimum, maximum


def longest_run(stalls):
    group = itertools.groupby(stalls)
    result = []
    index = 0
    for k, g in group:
        if k == 0:
            length = len(list(g))
            result.append((length, index))
            index += length
        else:
            index += len(list(g))
    return max(result, key=lambda a: a[0])

def min_max_from_run(n):
    minimum = math.ceil(n/2) - 1
    maximum = n - minimum - 1
    return minimum, maximum


def main(infile, outfile):
    with open(infile, 'r') as input, open(outfile, 'w') as out:
        num_cases = int(input.readline())
        for case in range(1, num_cases+1):
            out.write('Case #{}: '.format(case))

            N, K = (int(x) for x in input.readline().rstrip().split())

            stalls = [1] + [0] * N + [1]
            for i in range(K):
                index, minimum, maximum = choose2(stalls)
                stalls[index] = 1

            out.write(str(maximum) + ' ' + str(minimum) + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="codejam qual C")
    parser.add_argument('-i', '--input', type=str,
                        help='Input file')
    parser.add_argument('-o', '--output', type=str,
                        help='Output file')
    args = parser.parse_args()
    main(args.input, args.output)
