#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = "Régis Décamps"
import sys
import math


def is_palindrome(int):
    s = str(int)
    return s == s[::-1]


def count_fair_square(a, b):
    counter = 0
    # optim if I search x in [a b] so that sqrt(x) is also a palindrome
    # it is faster to search i in [sqrt(a), sqrt(b)] so that i**2 is alsi a palindrome
    for i in range(math.ceil(math.sqrt(a)), math.ceil(math.sqrt(b))+1):
        sq = i**2
        if a<=sq and sq<=b:
            if is_palindrome(i) and is_palindrome(sq):
                counter += 1

    return counter


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        nb_tests = int(f.readline())
        for i in range(1, nb_tests + 1):
            min, max = f.readline().split(' ')
            count = count_fair_square(float(min), float(max))
            print("Case #{i}: {c}".format(i=i, min=min, max=max, c=count))