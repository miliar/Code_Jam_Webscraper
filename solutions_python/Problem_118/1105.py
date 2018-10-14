#!/usr/bin/env python
import fileinput
from math import sqrt, floor, ceil


def getlines():
    inp = fileinput.input()
    for line in inp:
        yield map(int, line.rstrip().split())

getline = getlines()
cases = getline.next()[0]


def is_palindrome(num):
    s = str(num)
    return s == s[::-1]


for case in range(cases):
    x, y = getline.next()
    a = int(floor(sqrt(x)))
    b = int(ceil(sqrt(y)))
    result = 0
    for num in xrange(a, b + 1):
        square = num * num
        if square >= x and square <= y and is_palindrome(square) \
           and is_palindrome(num):
            result += 1
    print("Case #%d: %s" % (case + 1, result))
