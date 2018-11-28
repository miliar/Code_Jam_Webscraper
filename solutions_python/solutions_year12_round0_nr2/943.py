#!/usr/bin/env python



import argparse
import sys
from itertools import combinations


def solve(line):
    line = map(int, line.split())
    googlers = line[0]
    surprising = line[1]
    best_result = line[2]
    results = line[3:]
    counter = 0
    for result in results:
        if max(normal_score(result)) >= best_result:
            counter += 1
            continue
        elif surprising != 0:
            if max(surprising_score(result)) >= best_result:
                counter += 1
                surprising -= 1
    return counter
    # return (googlers, surprising, best_result,
    #         results, map(normal_score, results), map(surprising_score, results), counter)


def normal_score(result):
    base = result / 3
    if result % 3 == 0:
        return (base, base, base)
    elif result % 3 == 1:
        return (base, base, base + 1)
    else:
        return (base, base + 1, base + 1)


def surprising_score(result):
    base = result / 3
    if result % 3 == 0:
        if base:
            return (base - 1, base, base + 1)
        else:
            return normal_score(result)
    elif result % 3 == 1:
        if base:
            return (base - 1, base + 1, base + 1)
        else:
            return normal_score(result)
    else:
        return (base, base, base + 2)


def main(args):
    test_cases = next(args.input).strip()
    for case_index, line in enumerate(args.input, 1):
        print("Case #{}: {}".format(case_index, solve(line.strip())))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=argparse.FileType('r'), default=sys.stdin)
    main(parser.parse_args())
