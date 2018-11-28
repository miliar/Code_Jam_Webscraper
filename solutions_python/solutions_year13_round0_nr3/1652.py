#!/usr/bin/python

import sys, math

def is_fair(integer):
    text = str(integer)
    return text == text[::-1]

def solve(FS, case):
    (lower, upper) = (int(case[0]), int(case[1]))
    return len(filter(lambda i: i >= lower and i <= upper, FS))

FS = set()
for i in range(1, int(math.sqrt(10 ** 14))):
    if is_fair(i) and is_fair(i ** 2):
        FS.add(i ** 2)

input = [line.strip().split() for line in sys.stdin]
for index in range(1, int(input[0][0]) + 1):
    print 'Case #%d: %d' % (index, solve(FS, input[index]))
