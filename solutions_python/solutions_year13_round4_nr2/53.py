#!/usr/bin/env python
# coding=utf-8
from __future__ import print_function
from sys import stdin, stdout

def compute_min(n, p):
    if n == 0:
        return 0
    if n == 1:
        return p-1
    if 2**n == p: return 2**n - 1
    if p <= 2**(n-1):
        return 0
    else:
        return 2 * compute_min(n-1, p - 2**(n-1)) + 2

def compute_max(n, p):
    if n == 0:
        return 0
    if n == 1:
        return p-1
    if 2**n == p: return 2**n - 1
    if p <= 2**(n-1):
        return 2 * compute_max(n-1, p)
    else:
        return 2**n - 2

def solve():
    n,p = map(int, stdin.readline().strip().split())
    return "{0} {1}".format(compute_min(n, p), compute_max(n, p))

if __name__ == "__main__":
    n = int(stdin.readline())
    for i in range(n):
        print("Case #{0}: {1}".format(i+1, solve()))
