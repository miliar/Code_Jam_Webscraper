#!/usr/bin/env python
#-*- coding:utf-8 -*-

from itertools import product
import sys

get_ints = lambda f:map(int, next(f).strip().split(' '))

def is_palindromes(i):
    s = str(i)
    return all(s[j] == s[-1 - j] for j in range(len(s)/2))

def all_above(n):
    S1, S2 = [(1, ), (2, ), (3, )], [(1, ), (2,)]
    yield 1
    yield 4
    yield 9
    yield 121
    yield 484
    for i in range(1, n):
        new_S1, new_S2 = [], []
        for x in S1:
            for j in range(3):
                p = x + (j, )
                SQ_N1 = sum((p[j] if j < len(p) else p[2 * i - j]) * 10 ** j  for j in range(2 * i + 1)) ** 2
                if is_palindromes(SQ_N1):
                    yield SQ_N1
                    new_S1.append(p)

        for x in S2:
            for j in range(3):
                p = x + (j, )
                SQ_N2 = sum((p[j] if j < len(p) else p[2 * i + 1 - j]) * 10 ** j for j in range(2 * i + 2)) ** 2
                if is_palindromes(SQ_N2):
                    yield SQ_N2
                    new_S2.append(p)
        S1, S2 = new_S1, new_S2

def get_input(f):
    T = int(next(f))
    for _ in range(T):
        A, B = get_ints(f)
        yield A, B

def main():
    Fare_squares = set(all_above(26))
    for i, (A, B) in enumerate(get_input(sys.stdin)):
        print "Case #{0}:".format(i + 1), len(filter(lambda v:A<=v<=B, Fare_squares))

if __name__ == "__main__":
    main()
