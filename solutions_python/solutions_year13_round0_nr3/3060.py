#!/usr/bin/env python

"""
Solution to problem D of Google Codejam 2013
"""

from sys import argv
from os import getcwd, path


def is_palindrome(n):
    n = str(n)
    return n == n[::-1]


def take_input():
    with open(path.join(getcwd(), argv[1]+'.in'), 'r') as inp:
        lines = inp.readlines()
    return lines[1:]


def fair_and_square(i, j):
    count = 0
    for n in xrange(int(i), int(j)+1):
        n_sqrt = n ** 0.5
        if is_palindrome(n) and (n_sqrt == int(n_sqrt)) and is_palindrome(int(n_sqrt)):
            count += 1
    return count


if __name__ == '__main__':
    inp = take_input()
    with open(path.join(getcwd(), argv[1]+'.out'), 'w') as out:
        for i, case in enumerate(inp):
            values = map(int, case.split())
            count = fair_and_square(*values)
            out.writelines('Case #{0}: {1}\n'.format(i+1, count))
    print 'Done'
