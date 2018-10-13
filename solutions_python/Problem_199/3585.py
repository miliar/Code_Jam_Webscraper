#!/usr/bin/env pypy
import sys
import os
import argparse

PARSER = argparse.ArgumentParser()
PARSER.add_argument("input_file",
                    metavar="INPUT_FILE",
                    nargs='?',
                    type=argparse.FileType('r'),
                    default=sys.stdin)
PARSER.add_argument("output_file",
                    metavar="OUTPUT_FILE",
                    nargs='?',
                    type=argparse.FileType('w'),
                    default=sys.stdout)
ARGS = PARSER.parse_args()

def verify(s):
    return not '-' in s

def inverse(c):
    return '-' if c == '+' else '+'

def flip(s, k, i):
    new_s = s[:i]
    for index in range(k):
        new_s += inverse(s[i+index])
    new_s += s[i+k:]
    return new_s

def check(s, k):
    flip_count = 0
    while True:
        if verify(s):
            return flip_count
        index = s.index('-')
        try:
            s = flip(s, k, index)
        except IndexError:
            return "IMPOSSIBLE"
        flip_count += 1

for index, l in enumerate(ARGS.input_file.readlines()[1:]):
    l = l.strip()
    S, K = l.split()
    K = int(K)
    result = check(S, K)
    ARGS.output_file.write("Case #{}: {}\n".format(index + 1, result))
