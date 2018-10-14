#!/usr/bin/env python
# coding: utf-8

import sys

BAD_MAGICIAN = "Bad magician!"
VOLUNTEER_CHEATED = "Volunteer cheated!"
INPUT = open(sys.argv[1], 'r')


def matrix():
    result = []
    while len(result) < 4:
        result.append([int(value) for value in INPUT.readline().split(" ")])
    return result


def guess():
    first_answer = int(INPUT.readline()) - 1
    first_answer = matrix()[first_answer]
    second_answer = int(INPUT.readline()) - 1
    second_answer = matrix()[second_answer]
    result = [value for value in first_answer if value in second_answer]
    if not len(result):
        return VOLUNTEER_CHEATED
    if len(result) is 1:
        return result[0]
    return BAD_MAGICIAN


def __main__():
    case_number = 0
    result = "Case #%d: %s"
    tests = int(INPUT.readline())
    while case_number < tests:
        case_number += 1
        print result % (case_number, guess())


if __name__ == "__main__":
    __main__()
