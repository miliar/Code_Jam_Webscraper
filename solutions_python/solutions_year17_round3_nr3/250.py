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
import math
from collections import Counter
from operator import mul


def parse_line(line):
    words = line.split()
    return [float(e) for e in words]

def parse_input(input_file):
    data = []
    with open(input_file) as f:
        lines = [e.strip() for e in f.readlines()]
    t = int(lines[0])
    count = 1
    for i in range(t):
        n, k = [int(e) for e in lines[count].split()]
        u = float(lines[count+1])
        cores = parse_line(lines[count+2])
        count = count + 3
        data.append((k, u, sorted(cores)))
    return data


def prob(k, cores):
    if k == sum([e[1] for e in cores]):
        return reduce(mul, [e[0] ** e[1] for e in cores], 1)



def solve_first(k, u, cores):
    # k == len(cores)
    # [(p, nb_cores), ...]
    cores = [[i, v] for i, v in sorted(Counter(cores).items())]
    while u > 0:
        if len(cores) > 1:
            step = cores[1][0] - cores[0][0]
            nb_to_up = cores[0][1]
            if u > step * nb_to_up:
                cores = cores[1:]
                cores[0][1] += nb_to_up
            else:
                step = u / nb_to_up
                cores[0][0] += step
            u -= step * nb_to_up
        else:
            cores[0][0] += u / cores[0][1]
            break
    p = prob(k, cores)
    print('prob', p)
    return p

def output(results):
    o = ''
    for i, r in enumerate(results):
        o += 'Case #%d: %f\n' % (i+1, r)
    return o


def main(input_file):

    data = parse_input(input_file)
    results = []
    for example in data:
        print(example)
        results.append(solve_first(*example))
    print(results)

    with open("results/%s" % os.path.basename(input_file), 'w') as f:
        f.write(output(results))

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('file')
    args = parser.parse_args()
    main(args.file)

