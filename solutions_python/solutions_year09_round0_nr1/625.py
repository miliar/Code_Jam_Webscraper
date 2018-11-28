#!/usr/bin/env python

import re

inFile = './A-large.in'

input = open(inFile, 'r').readlines()
(L,D,N) = input[0].strip().split()
L = int(L)
D = int(D)
N = int(N)

try:
    assert 1 <= L <= 15
except AssertionError:
    print 'L is out of range'

try:
    assert 1 <= D <= 5000
except AssertionError:
    print 'D is out of range'

try:
    assert 1 <= N <= 500
except AssertionError:
    print 'N is out of range'

words = input[1:D+1]
cases = input[D+1:D+N+1]

count = 0
trial = 1

outFile = './small.out'
output = open(outFile, 'w')

for case in cases:
    case = case.strip()
    case = case.replace('(', '[')
    case = case.replace(')', ']')
    pattern = re.compile(case)
    for word in words:
        word = word.strip()
        match = pattern.match(word)
        if match: count += 1
    out = 'Case #%s: %s\n' % (trial, count)
    output.write(out)
    trial += 1
    count = 0

output.close()
