#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Problem

# Do you ever become frustrated with television because you keep seeing the same things, recycled over and over again? Well I personally don't care about television, but I do sometimes feel that way about numbers.

# Let's say a pair of distinct positive integers (n, m) is recycled if you can obtain m by moving some digits from the back of n to the front without changing their order. For example, (12345, 34512) is a recycled pair since you can obtain 34512 by moving 345 from the end of 12345 to the front. Note that n and m must have the same number of digits in order to be a recycled pair. Neither n nor m can have leading zeros.

# Given integers A and B with the same number of digits and no leading zeros, how many distinct recycled pairs (n, m) are there with A ≤ n < m ≤ B?

# Input

# The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of a single line containing the integers A and B.

# Output

# For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1), and y is the number of recycled pairs (n, m) with A ≤ n < m ≤ B.

# Limits

# 1 ≤ T ≤ 50.
# A and B have the same number of digits.

# Small dataset

# 1 ≤ A ≤ B ≤ 1000.

# Large dataset

# 1 ≤ A ≤ B ≤ 2000000.

# Sample


# Input 
 	
# Output 
 
# 4
# 1 9
# 10 40
# 100 500
# 1111 2222

# Case #1: 0
# Case #2: 3
# Case #3: 156
# Case #4: 287



import sys


def generate_rings(sv):
    for i in range(len(sv)):
        yield sv[i:]+sv[:i]

def unique_cycles(v):
    sv = str(v)
    assert sv[0] != '0'
    return set(int(r) for r in generate_rings(sv) if r[0] != '0')

def solve_n(n, b):
    if n >= b:
        return 0
    cycles = unique_cycles(n)
    return sum(1 for m in cycles if n < m <= b)

def solve(a, b):
    return sum(solve_n(n, b) for n in range(a, b+1))


# print unique_cycles(12345)
# print unique_cycles(12245)
# print unique_cycles(14245)
# print unique_cycles(1212)
# print unique_cycles(11111)
# print unique_cycles(2)

count_skipped = False
for n, line in enumerate(sys.stdin):
    if not count_skipped:
        count_skipped = True
        continue

    A, B = [ int(s) for s in line.split() ]

    ans = solve(A, B)

    print 'Case #%d: %d' % (n, ans)
    sys.stdout.flush()

