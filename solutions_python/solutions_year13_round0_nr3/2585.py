#!/usr/bin/env python3

import sys, math

def read_integers():
    n = 0
    with open(sys.argv[1]) as input_file:
        n = int(input_file.readline().strip())
        cases = []
        for l in input_file.readlines():
            cases.append(tuple([int(e) for e in l.strip().split()]))

    return n, cases

def is_palindrome(n):
    binary = []
    while(n > 0):
        binary.append(n % 10)
        n = int(n/10)
    return binary == binary[::-1]

def is_square(n):
    return int(math.sqrt(n)) * int(math.sqrt(n)) == n

n, cases = read_integers()

for i in range(n):
    min_n, max_n = cases[i]
    n = 0

    for number in range(min_n, max_n+1):
        if is_palindrome(number) and is_square(number) \
            and is_palindrome(math.sqrt(number)):
            n += 1

    print("Case #{}: {}".format(i+1, n))
