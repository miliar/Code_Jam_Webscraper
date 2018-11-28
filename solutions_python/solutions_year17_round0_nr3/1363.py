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
from math import log, ceil, floor

from tqdm import tqdm

def parse_line(line):
    return [int(e) for e in line.split()]


def parse_input(input_file):
    data = []
    with open(input_file) as f:
        lines = [e.strip() for e in f.readlines()]
    nb = int(lines[0])
    for i in range(nb):
        data.append(parse_line(lines[i+1]))
    return data


def argmax(iterable):
    results = []
    M = 0
    for i, e in enumerate(iterable):
        if e > M:
            M = e
            results = [i]
        if e == M:
            results.append(i)
    return results



def place(s):
    n = float(s) / 2.
    if s%2 ==0:
        return n, n-1
    else:
        return int(n), int(n)


def solve(example):
    s, p = example
    if p == 1:
        return place(s)
    stalls_taken = [0, s+1]
    m, M = 0, 0
    indices = []
    etage = int(log(p, 2))
    nb_prec = 2**etage - 1
    print('etage', etage, 'nb_prec', nb_prec)
    places_left = s - nb_prec
    print('places left', places_left)
    intervals = [0 for i in range(2**etage)]

    for i in range(places_left):
        intervals[i % len(intervals)] += 1

    good_interval = intervals[p - nb_prec - 1]
    print('good_interval', good_interval)
    return place(good_interval)


def output(results):
    o = ''
    for i, r in enumerate(results):
        o += 'Case #%d: %d %d\n' % (i+1, r[0], r[1])
    return o


def main(input_file):

    data = parse_input(input_file)
    results = []
    for example in tqdm(data):
        print("Case: %s" % example)
        results.append(solve(example))
        print('Case: %d %d\n' % (results[-1][0], results[-1][1]))

    with open("results/%s" % os.path.basename(input_file), 'w') as f:
        f.write(output(results))

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('file')
    args = parser.parse_args()
    main(args.file)

