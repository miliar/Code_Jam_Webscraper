#! /usr/local/bin/python3.5

import sys

import copy


def sol_print(value):
    sol_print.line_number += 1
    print("Case #%d: %s" % (sol_print.line_number, value))


sol_print.line_number = 0

T = int(input())


def fill_with_nine(N, pos):
    for i in range(pos, len(N)):
        N[i] = 9


def solve(N):
    for i in range(len(N) - 1, 0, -1):

        if N[i] < N[i - 1]:
            fill_with_nine(N, i)
            N[i - 1] -= 1

    return int("".join([str(x) for x in N]))


for i in range(T):
    N = [int(x) for x in list(input())]

    sol_print(solve(N))
