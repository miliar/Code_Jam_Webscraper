#!/usr/bin/env python3
# coding=utf-8

"""
  Solution to Qualification Round.C

  Author: killerrex@gmail.com
"""

import sys


# Clarify
q1 = 1
qi = 2
qj = 3
qk = 4
_rep = {'i': qi, 'j': qj, 'k': qk}

#
# To avoid dozens of dict queries,m map letters as:
# '1' -> 1  'j' -> 3
# 'i' -> 2  'k' -> 4
# 0 -> Nothing
_qmap = [
    None,
    [None, q1, qi, qj, qk],  # 1*1 *i 1*j 1*k
    [None, qi, -q1, qk, -qj],
    [None, qj, -qk, -q1, qi],
    [None, qk, qj, -qi, -q1]
]


def qprod(a, b):
    """
    Clumsy Quat product
    :param a:
    :param b:
    :return:
    """
    s = 1
    if a < 0:
        s = -1

    if b < 0:
        s *= -1

    return s*_qmap[abs(a)][abs(b)]


def correct(ijk, x):
    """
    Try to solve a case
    :param ijk:
    :return: YES/NO
    """
    if len(ijk)*x < 3:
        return "NO"

    # Notice that a valid set all the letters multiplication
    # must be equal to i*j*k = 1 to be valid (although it is not enough)
    # So every subset that multiply 1 can be ignored
    v = 1
    level = 2
    for loop in range(x):
        for l in ijk:
            # Get next product
            v = qprod(v, l)

            if level == v:
                v = 1
                level += 1

    # At the end must be:
    #  level = 5 => Means we jhave found i, j k in order
    #  v = 1 => Means after the k all elements multiply to 1

    if level == 5 and v == 1:
        return "YES"
    else:
        return "NO"


def solve(fd):
    """
    Solve for the complete file
    :param fd:
    :return:
    """

    cases = int(fd.readline().strip())

    for k in range(cases):
        l, x = [int(s) for s in fd.readline().strip().split()]
        txt = fd.readline().strip()
        assert(len(txt) == l)

        ijk = [_rep[c] for c in txt]
        print("Case #{}: {}".format(k+1, correct(ijk, x)))


if __name__ == '__main__':

    # Read stdin and write stdout
    solve(sys.stdin)
