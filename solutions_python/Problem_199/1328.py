#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 antoine <antoine@antoine-HP>
#
# Distributed under terms of the MIT license.

"""
Problem A  - Oversized Pancake Flipper
"""

import argparse
import os


def parse_line(line):
    words = line.split()
    return (list(words[0]), int(words[1]))

def parse_input(input_file):
    data = []
    with open(input_file) as f:
        lines = [e.strip() for e in f.readlines()]
    print(lines)
    nb = int(lines[0])
    for i in range(nb):
        data.append(parse_line(lines[i+1]))
    return data


def flip(x):
    if x == '-':
        return '+'
    else:
        return '-'

def solve(example):
    p, k = example
    result = 0
    print(''.join(p))
    for i in range(len(p) - k + 1):
        if p[i] == '-':
            p[i:i+k] = map(flip, p[i:i+k])
            result += 1
            print(i, ''.join(p), result)
    if all([e == '+' for e in p]):
        return result
    else:
        return -1

def output(results):
    o = ''
    for i, r in enumerate(results):
        o += 'Case #%d: ' % (i+1)
        if r == -1:
            o += "IMPOSSIBLE\n"
        else:
            o += "%d\n" % r
    return o


def main(input_file):

    data = parse_input(input_file)
    results = []
    for example in data:
        results.append(solve(example))
    print(results)

    with open("results/%s" % os.path.basename(input_file), 'w') as f:
        f.write(output(results))

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('file')
    args = parser.parse_args()
    main(args.file)

