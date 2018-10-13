#!/usr/bin/python

# vim: set expandtab shiftwidth=4 tabstop=4:

import sys
import math
import itertools
import gmpy2
import cProfile

palindromes = {}
square_palindromes = set()

def populate(limit):
    for n in itertools.count(1):
        if n > limit:
            break
        if not is_palindrome(n):
            continue
        square = gmpy2.square(n)
        if square > limit:
            break
        if is_palindrome(square):
            square_palindromes.add(square)

def solve2(a, b):
    count = 0
    for n in square_palindromes:
        if n >= a and n <= b:
            count += 1
    return count

def solve(a, b):
    count = 0
    for n in itertools.count(a):
        if n % 1000000 == 0:
            print 'At ' + str(n)
        if n > b:
            break
        if not is_palindrome(n):
            continue
        if is_palindrome(is_square(n)):
            count += 1
    return count

def is_palindrome(n):
    if n == '':
        return True
    if not n:
        return False
    if n in palindromes:
        return palindromes[n]
    n_str = str(n)
    palindromes[n] = (n_str[0] == n_str[-1] and is_palindrome(n_str[1:-1]))
    return palindromes[n]

def is_square(n):
    n = gmpy2.mpz(n)
    root = gmpy2.isqrt(n)
    if gmpy2.square(root) == n:
        return root
    else:
        return None

def solve_all(input_file):
    count = int(input_file.readline().strip())
    populate(10**14)
    for count in range(1, count + 1):
        a, b = [int(s) for s in input_file.readline().strip().split()]
        print 'Case #{}: {}'.format(count, solve2(a, b))

solve_all(open(sys.argv[1]))
