#!/usr/bin/python

import sys

def print_ans(test, ans, file):
    file.write("Case #{0}: {1}\n".format(test, ans))

def good(n):
    prev = 10
    while n > 0:
        if n%10 <= prev:
            prev = n%10
            n /= 10
        else:
            return False
    return True

def slow(n):
    if n > 1e8:
        return fast(n)
    while not good(n):
        n -= 1
    return n

def fast(n):
    sn = str(n)
    l = len(sn)
    if good(n):
        return n
    for common in xrange(l-1, -1, -1):
        pref = sn[:common]
        if sn[common] != '0':
            res = int(pref + str(int(sn[common]) - 1) + '9' * (l - common - 1))
            if good(res):
                return res
    return int('9'* (l - 1))



with open("input.txt") as input:
    tests = int(input.readline())
    with open("output.txt", 'w') as output:
        for test in xrange(1, tests + 1):
            n = int(input.readline())
            ans = slow(n)
            if ans != fast(n):
                assert ans == fast(n)
            print_ans(test, ans, output)
