#!/usr/bin/env python
from sys import stdin, stdout
from itertools import *
from bisect import bisect

def in_range(A, B, nums):
    return bisect(nums, B) - bisect(nums, A-1)

def answer(data):
    global efs, ofs
    A,B = data
    return in_range(A, B, efs) + in_range(A, B, ofs)

def cases(s):
    while 1:
        A,B = map(int, next(s).rstrip().split())
        yield (A,B)

efs = []
ofs = []

def is_palindromic(n):
    s = str(n)
    return s == ''.join(reversed(s))

def update_f_and_s(f_and_s, n):
    ns = n*n
    if is_palindromic(ns):
        f_and_s.append(ns)

for n in range(1, 10**5):
    if n%10 == 0:
        continue
    s = str(n)
    rs = ''.join(reversed(s))

    even_len = int(rs+s)
    update_f_and_s(efs, even_len)
    odd_len = int(rs[:-1] + s)
    update_f_and_s(ofs, odd_len)

if __name__ == '__main__':
    stdin.next()
    for n,case in enumerate(cases(stdin)):
        print "Case #%d: %s" % (n+1, answer(case))
