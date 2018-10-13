#!/usr/bin/env python
# coding=utf-8
from __future__ import print_function
from sys import stdin, stdout


def is_palindrome(n):
    return list(str(n)) == list(reversed(str(n)))

def is_square(n):
    return int(n**0.5)**2 == n

def solve(a, b):
    b += 1
    res = 0
    for n in range(a, b):
        if is_square(n) and is_palindrome(n) and is_palindrome(int(n**0.5)):
            res += 1
    return res

if __name__ == "__main__":
    t = int(stdin.readline())
    for i in range(t):
        (a, b) = map(int, stdin.readline().strip().split())
        print("Case #{0}: {1}".format(i+1, solve(a, b)))
