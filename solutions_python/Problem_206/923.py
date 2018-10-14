#!/usr/bin/env python3
# coding=utf-8

"""
    Solve Quals 2017 p.A

    Author: killerrex
"""

import sys


def read_int(fd):

    txt = fd.readline().split()

    return (int(s) for s in txt)


def read_case(fd):

    d, n = read_int(fd)

    horses = []
    for k in range(n):
        horses.append(read_int(fd))

    return d, horses


def solve(fd):
    total = int(fd.readline().strip())

    for j in range(total):
        # Read next problem
        d, horses = read_case(fd)

        # Get the lowest possible speed
        speed = None
        for k, s in horses:
            if k == d:
                # This one does not matter
                continue

            opt = s / ( 1 - k/d)

            if speed is None or opt < speed:
                speed = opt
        print("Case #{}: {:.6f}".format(j+1, speed))


def start():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as fd:
            solve(fd)
    else:
        solve(sys.stdin)


if __name__ == '__main__':
    start()
