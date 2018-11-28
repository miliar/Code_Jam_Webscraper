#!/usr/bin/env python3
import numpy


def stats(s):
    r = [0] * 26
    for c in s:
        r[ord(c) - ord('A')] += 1
    return r


def build():
    strs = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    a = numpy.zeros((26, 10))
    for j in range(len(strs)):
        st = stats(strs[j])
        for i in range(len(st)):
            a[i][j] = st[i]
    return a


def solve(inp):
    b = stats(inp)
    vals = numpy.linalg.lstsq(A, b)[0]
    r = str()
    for i in range(10):
        n = int(vals[i] + 0.5)
        r += chr(ord('0') + i) * n
    return r


def main():
    import sys
    i = 1
    for line in sys.stdin.readlines()[1:]:
        print('Case #' + str(i) + ': ' + solve(line.strip()))
        i += 1

A = build()
main()
