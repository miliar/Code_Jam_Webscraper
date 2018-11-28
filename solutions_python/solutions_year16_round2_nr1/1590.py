# -*- coding: utf-8 -*-

"""\

┻┻︵⁞=༎ຶ﹏༎ຶ=⁞︵┻┻


"""

from __future__ import print_function

import argparse
from collections import defaultdict


def readl(f):
    return f.next().strip()

mapping = {
    "ZERO": 0,
    "ONE": 1,
    "TWO": 2,
    "THREE": 3,
    "FOUR": 4,
    "FIVE": 5,
    "SIX": 6,
    "SEVEN": 7,
    "EIGHT": 8,
    "NINE": 9
}


def process(line):
    occs = defaultdict(int)
    for c in line:
        occs[c] += 1
    return rec(occs, '', ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"))


def dec(occs, digit):
    result = occs.copy()
    for y in digit:
        result[y] -= 1
    return result


def rec(occs, phone, digits):
    if all(map(lambda x: x == 0, occs.values())):
        return phone
    if not digits:
        return False
    digit = digits[0]
    if len(filter(lambda x: occs[x] >= 1, digit)) == len(digit):
        next_number = rec(dec(occs, digit), phone + str(mapping[digit]), digits[1:])
        if next_number:
            return next_number
        reuse_number = rec(dec(occs, digit), phone + str(mapping[digit]), digits)
        if reuse_number:
            return reuse_number
    skip_number = rec(occs, phone, digits[1:])
    if skip_number:
        return skip_number


def output_results(results, f):
    for i, res in enumerate(results):
        print("Case #%s: %s" % (i + 1, res), file=f)


def solve(f):
    test_cases = readl(f)
    results = []
    try:
        while True:
            n = readl(f)
            results.append(process(n))
    except StopIteration:
        pass
    return results


def main():
    # TODO: fix positional args
    parser = argparse.ArgumentParser(description='The prices are mixed!')
    parser.add_argument('file', type=str, help='the input', default='./data/in')
    parser.add_argument('output', type=str, help='the output', default='./data/out')
    args = parser.parse_args()
    with open(args.file) as f:
        x = solve(f)
    with open(args.output, 'w') as f:
        output_results(x, f)


if __name__ == '__main__':
    main()

