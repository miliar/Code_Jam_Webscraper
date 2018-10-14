#! /usr/local/bin/python3.5

import sys

import copy


def sol_print(value):
    sol_print.line_number += 1
    print("Case #%d: %s" % (sol_print.line_number, value))


sol_print.line_number = 0

HAPPY = "+"
BLANK = "-"

T = int(input())


def flip_line(line, K, pos):
    for i in range(K):
        if line[pos + i] == HAPPY:
            line[pos + i] = BLANK
        else:
            line[pos + i] = HAPPY


def solve(line, K):
    res = 0
    for i in range(len(line) - K + 1):
        if line[i] == BLANK:
            res += 1
            flip_line(line, K, i)

    if BLANK in line:
        return "IMPOSSIBLE"
    return res


for i in range(T):
    line, K = input().split()
    line = list(line)
    K = int(K)

    sol_print(solve(line, K))
