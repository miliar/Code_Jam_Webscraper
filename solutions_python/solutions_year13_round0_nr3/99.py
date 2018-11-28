# use pypy!

import sys
import random

#sys.stdin = open("C-small-attempt0.in")

n_cases = input()

def to_ints(s):
    return map(int, s.split())

# precompute!

# http://oeis.org/A057135
# Palindromes whose square is a palindrome;
# also palindromes whose sum of squares of digits is less than 10.

def square_palins(maxlen, curt):
    assert maxlen >= 0
    if curt != 0:
        yield ''
    for n in (0, 1, 2, 3):
        if n == 0 and curt == 0:
            # no trailing zeros
            yield '0'
            continue
        if curt + n * n < 10:
            yield str(n)
        if maxlen >= 2 and curt + 2 * n * n < 10:
            s = str(n)
            for sub in square_palins(maxlen - 2, curt + 2 * n * n):
                yield s + sub + s

palins = sorted(int(x) for x in square_palins(50, 0))
palin_squares = [x ** 2 for x in palins]

for x in palin_squares:
    assert str(x) == str(x)[::-1]

for case in xrange(1, n_cases + 1):
    a, b = to_ints(raw_input())

    out = sum(1 for x in palin_squares if a <= x <= b)

    print "Case #%d: %s" % (case, out)
