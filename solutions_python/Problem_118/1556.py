#!/usr/bin/python

import sys
from math import sqrt


fair_and_squares = []

def isPalindrome (num):
    if num < 10:
        return True

    s = str(num)
    l = len(s)
    if l % 2 == 0:
        return s[:l/2] == s[l/2:][::-1]
    else:
        return s[:l/2] == s[l/2+1:][::-1]


def buildFairAndSquare (maxB):
    global fair_and_squares
    i = 0
    while 1:
        square = i**2
        if square > maxB:
            break
        if isPalindrome(i) and isPalindrome(square):
            # print str(square) + " is fair and square (" + str(i) + " being a palindrome)"
            if square not in fair_and_squares:
                fair_and_squares.append(square)
        i += 1
    fair_and_squares.sort()


def solve_case (A, B):
    global fair_and_squares
    res = 0

    for r in fair_and_squares:
        if r < A:
            continue
        if r > B:
            break
        res += 1

    return res


def solve_input (fname):
    f = open(fname, 'r')
    f.readline()

    maxB = 0
    cases = []
    for line in f:
        s = line.split()
        A,B = map(int, s)
        maxB = max(maxB, B)
        cases.append((A,B))

    buildFairAndSquare (maxB)

    caseNum = 1
    for c in cases:
        A,B = c
        print "Case #" + str(caseNum) + ": " + str(solve_case(A, B))
        caseNum += 1

    f.close()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        fname = sys.argv[1]
    else:
        fname = 'Csample'

    solve_input(fname)

