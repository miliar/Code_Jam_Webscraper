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


def parse_line(line):
    words = line.split()
    return int(words[0]), int(words[1])

def parse_input(input_file):
    data = []
    with open(input_file) as f:
        lines = [e.strip() for e in f.readlines()]
    t = int(lines[0])
    c = 1
    for i in range(t):
        n, k = parse_line(lines[c+i])
        pancakes = []
        for j in range(n):
            pancakes.append(parse_line(lines[c+i+1+j]))
        c = c + n
        data.append((k, sorted(pancakes)))
    return data


def area(stack):
    a = stack[0][0] * stack[0][0]
    a += 2 * sum(e[0] * e[1] for e in stack)
    return a * math.pi



def solve(k, sorted_pancakes):
    sorted_pancakes = sorted([(e[0], e[1], e[0]*e[1]) for e in sorted_pancakes], key=lambda x: x[2], reverse=True)

    stack = []
    score = 0.0
    for i in range(len(sorted_pancakes)):
        r_max = sorted_pancakes[i][0]
        new_stack = [sorted_pancakes[i]] + \
            [e for e in sorted_pancakes[:i]+sorted_pancakes[i+1:] if e[0] <= r_max][:k-1]
        if len(new_stack) == k:
            new_score = area(new_stack)
            if new_score > score:
                score = new_score
                stack = new_stack
    return score

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
        results.append(solve(*example))
    print(results)

    with open("results/%s" % os.path.basename(input_file), 'w') as f:
        f.write(output(results))

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('file')
    args = parser.parse_args()
    main(args.file)

