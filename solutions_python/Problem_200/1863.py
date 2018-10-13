#!/usr/bin/python
# coding: utf8

"""
    Google Code Jam 2017 - Qualification round
    Problem B
"""

from sys import stdin


def is_tidy(x):
    cast = [int(c) for c in str(x)]
    for i in range(len(cast) - 1):
        if cast[i] > cast[i+1]:
            return False
    return True


def solve():
    n = []
    for c in stdin.readline():
        if c in '0123456789':
            n.append(int(c))
    # Edge case : n < 10.
    if len(n) == 1:
        return n[0]
    for i in range(len(n) - 1):
        if n[i] > n[i + 1]:
            if n[i] > n[i - 1]:
                n[i] -= 1
            else:
                k = i
                while k > 0 and n[k] == n[k - 1]:
                    n[k] = 9
                    k -= 1
                n[k] -= 1
            for j in range(i + 1, len(n)):
                n[j] = 9
    while len(n) > 1 and n[0] == 0:
        n = n[1:]
    result = ''
    for d in n:
        result += str(d)
    return result

if __name__ == '__main__':
    n = int(stdin.readline())
    for i in range(n):
        print('Case #%i: %s' % (i + 1, solve()))
