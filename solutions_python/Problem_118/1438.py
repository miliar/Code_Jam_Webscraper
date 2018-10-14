#!/usr/bin/env python

import fileinput
import math

input = fileinput.input()

def is_palindrome(num):
    return str(num) == str(num)[::-1]

assert is_palindrome('6')
assert is_palindrome('11')
assert is_palindrome('121')
assert not is_palindrome('123')

num_cases = int(input.next())
for case in xrange(1, num_cases + 1):
    lower, upper = map(int, input.next().split())
    i = int(math.ceil(math.sqrt(lower)))
    sq = i ** 2
    count = 0
    while sq <= upper:
        count += (is_palindrome(i) & is_palindrome(sq))
        i += 1
        sq = i ** 2
    print 'Case #%d: %d' % (case, count)
