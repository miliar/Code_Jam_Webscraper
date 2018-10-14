#!/usr/bin/python

import sys


def flip(c):
    if c == '-':
        return '+'
    elif c == '+':
        return '-'
    else:
        raise Exception("oops")


def flips(line, flipper):
    if flipper > len(line):
        for i in line:
            if i == '-':
                return -1
        return 0

    extra = 0
    if line[0] == '-':
        for i in range(flipper):
            line[i] = flip(line[i])

            extra = 1

    result = flips(line[1:], flipper)
    if result == -1:
        return -1

    return result + extra

def main():
    index = 0
    sys.setrecursionlimit(3000)
    sys.stdin.readline()
    for line in map(str.strip, sys.stdin.readlines()):
        # print line
        split = line.split()
        s, flipper = [c for c in split[0]], int(split[1])
        index += 1

        result = flips(s, flipper)
        if result == -1:
            result = "IMPOSSIBLE"
        print "Case #{}: {}".format(index, result)

    flips(['-'] * 2000, 10)
main()
