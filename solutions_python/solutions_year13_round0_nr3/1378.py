#!env python2

import math
import sys


def is_palindrome(n):
    s = str(n)
    length = len(s)

    if length % 2 == 0:
        lower = int(length / 2)
        upper = lower
    else:
        lower = int(length / 2)
        upper = lower + 1

    return s[:lower] == s[upper:]


def is_fair_and_square(sqrt_n):
    return is_palindrome(sqrt_n) and is_palindrome(sqrt_n * sqrt_n)


def find_palindromes(a, b):
    start = int(math.sqrt(a))
    end = int(math.ceil(math.sqrt(b)))
    count = 0

    for sqrt_n in range(start, end + 1):
        n = sqrt_n * sqrt_n
        if n >= a and n <= b and is_fair_and_square(sqrt_n):
            count += 1

    return count


def read_input():
    for line in sys.stdin.readlines()[1:]:
        yield tuple(map(int, line.split(' ')))


case = 1
for a, b in read_input():
    count = find_palindromes(a, b)
    print "Case #%d: %d" % (case, count)
    case += 1
