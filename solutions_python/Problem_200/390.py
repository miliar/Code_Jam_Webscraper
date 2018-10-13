#!/usr/bin/env python3


def is_tidy(n):
    last = 0
    for c in str(n):
        if int(c) < last:
            return False
        last = int(c)
    return True


def long_increase(n):
    prev = '0'
    for c in n:
        if int(c) < int(prev[-1]):
            return prev[1:]
        prev += c
    return prev[1:]


def brute_force(n):
    last_tidy = 0
    for i in range(1, n + 1):
        if is_tidy(i):
            last_tidy = i
    return last_tidy


def optimal(n):
    n = str(n)
    prefix = long_increase(n)
    if len(prefix) == len(str(n)):
        return prefix
    while True:
        prefix = str(int(prefix) - 1)
        new_long = long_increase(prefix)
        if len(new_long) == len(prefix):
            break
        prefix = new_long
    while len(prefix) < len(n):
        prefix += '9'
    while prefix[0] == '0':
        prefix = prefix[1:]
    return prefix

def test_both():
    for n in range(1, 1001):
        b = str(brute_force(n))
        o = str(optimal(n))
        if b != o:
            print(b, o, n)


T = int(input())

for case in range(T):
    N = int(input())
    answer = optimal(N)
    print("Case #", case + 1, ": ", answer, sep='')
