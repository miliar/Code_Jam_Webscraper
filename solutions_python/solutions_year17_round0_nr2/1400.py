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
from operator import mul    # or mul=lambda x,y:x*y
from fractions import Fraction


def parse_line(line):
    return int(line)


def parse_input(input_file):
    data = []
    with open(input_file) as f:
        lines = [e.strip() for e in f.readlines()]
    nb = int(lines[0])
    for i in range(nb):
        data.append(parse_line(lines[i+1]))
    return data

def tidy(l):
    return all([l[i] <= l[i+1] for i in range(len(l)-1)])


def to_number(e):
    return ''.join([str(a) for a in e])



def solve(example):
    e = [int(n) for n in str(example)]
    N = len(e)
    if tidy(e):
        return int(''.join([str(a) for a in e]))

    while not tidy(e):
        last_changed = 0
        for i in range(len(e) - 1):
            if e[i] > e[i+1]:
                e[i] -= 1
                break_index = i
                break
        for i in range(break_index+1, len(e)):
            e[i] = 9
        print(to_number(e))
    return to_number(e).lstrip('0')


def output(results):
    o = ''
    for i, r in enumerate(results):
        o += 'Case #%d: %s\n' % (i+1, r)
    return o


def main(input_file):

    data = parse_input(input_file)
    results = []
    for example in data:
        print("Case: %d" % example)
        results.append(solve(example))
        print("Case: %s" % results[-1])

    with open("results/%s" % os.path.basename(input_file), 'w') as f:
        f.write(output(results))

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('file')
    args = parser.parse_args()
    main(args.file)

