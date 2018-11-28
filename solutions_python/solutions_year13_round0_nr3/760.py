#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bisect import *


def is_palindrom(nb):
    s = str(nb)
    return s == s[::-1]

def gen(m):
    i = 1
    while 1:
        n = i**2
        if n > m: break
        if is_palindrom(i):
            yield n
        i += 1
       

if __name__ == '__main__':
    maxi = 10**14
    lst = [n for n in gen(maxi) if is_palindrom(n)]
    n = int(input())
    for i in range(n):
        a, b = [int(_) for _ in input().strip().split(' ')]
        ret = [n for n in lst if a <= n <= b]
        print('Case #{}: {}'.format(i + 1, len(ret)))

