#!/usr/bin/env python

"""
Developed by Jormar Arellano <jormar.arellano@gmail.com>

Google Code Jam 2017

Problem TODO - TODO

Notes:
"""

import sys
import math
import operator
import collections


class _:

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return ""
    pass


def change(list, i, until):
    while i < until:
        list[i] = not list[i]
        i += 1
    return list


if __name__ == "__main__":
    n_cases = int(raw_input())  # read a line with a single integer

    for _i in xrange(n_cases):
        # Reading...
        S, K = [s for s in raw_input().split(" ")]
        K = int(K)
        SMapped = map(lambda x: True if x == '+' else False, S)
        limit = len(S) - K
        result = 0

        # Solving...
        for i, value in enumerate(SMapped):
            if i > limit:
                break

            if not value:
                change(SMapped, i, i+K)
                result += 1

        if not reduce(lambda acc, x: acc and x, SMapped, True):
            result = 'IMPOSSIBLE'

        # printing...
        sys.stderr.write("Case #%s: %s Done!\n" % (_i + 1, result))
        print "Case #%s: %s" % (_i + 1, result)
