#! /usr/bin/env python
from math import floor, ceil, sqrt


def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


def solve(a, b):
    # Downgrade bounds
    a, b = ceil(sqrt(float(a))), floor(sqrt(float(b)))
    n = 0
    while a <= b:
        if is_palindrome(a) and is_palindrome(a*a):
            n += 1
        a += 1
    return n

if __name__ == "__main__":
    for i in range(int(input())):
        n = solve(*(input().split()))
        print("Case #" + str(i+1) + ": " + str(n))
