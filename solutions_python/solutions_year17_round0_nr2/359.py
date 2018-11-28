#!/usr/bin/python

import sys

def keep_first(digits):
    for i in digits:
        if i > digits[0]:
            return True
        if i < digits[0]:
            return False

    return True

def find_tidy(digits):
    if len(digits) == 0:
        return []

    if keep_first(digits):
        return [digits[0]] + find_tidy(digits[1:])

    if digits[0] == 1:
        initial = []
    else:
        initial = [digits[0] - 1]

    return initial + [9] * (len(digits) - 1)

def main():
    index = 0
    sys.setrecursionlimit(3000)
    sys.stdin.readline()
    for line in map(str.strip, sys.stdin.readlines()):
        # print line
        digits = [int(c) for c in line]
        index += 1

        result = "".join(map(str, find_tidy(digits)))
        print "Case #{}: {}".format(index, result)

main()
