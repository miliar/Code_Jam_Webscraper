#!/usr/bin/env python



import argparse
import sys
from itertools import combinations



def main(args):
    test_cases = next(args.input).strip()
    for case_index, line in enumerate(args.input, 1):
        start, finish = map(int, line.strip().split())
        result = sum(are_recycled(pair) for pair in
                     combinations(xrange(start, finish + 1), 2))
        print("Case #{}: {}".format(case_index, result))


def are_recycled(pair):
    first, second = map(str, pair)
    for index in xrange(1, len(second)):
        if first == second[index:] + second[:index]:
            return True
    else:
        return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=argparse.FileType('r'), default=sys.stdin)
    main(parser.parse_args())
