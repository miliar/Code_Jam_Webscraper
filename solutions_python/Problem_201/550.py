#!/usr/bin/env python

import sys
import logging


class Impossible(Exception):
    pass


def print_result(result, i):
    sys.stdout.write("Case #%s: %s\n" % (i, result))


def readline():
    return sys.stdin.readline().rstrip('\n')


def splitline(fn=str):
    return map(fn, readline().split())


def seat(seats, people):
    size = max(seats)
    cnt = seats.pop(size)

    fragments = (size / 2, (size - 1) / 2)
    if cnt >= people:
        return fragments

    for s in fragments:
        c = seats.pop(s, 0)
        seats[s] = c + cnt

    return seat(seats, people - cnt)


def solve():
    N, K = splitline(int)
    return "%s %s" % seat({N: 1}, K)


def main():
    for i in xrange(int(readline())):
        try:
            res = solve()
        except Impossible:
            res = "IMPOSSIBLE"
        print_result(res, i + 1)


if __name__ == '__main__':
    main()
