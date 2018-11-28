#!/usr/bin/env python

import sys
import os

def is_palindrome(s):
    l = len(s)
    n = l / 2
    i = 0
    while i < n:
        if s[i] != s[l - 1 - i]:
            return False
        i += 1
    return True

def fair_and_square(n):
    result = []
    if os.path.exists("pal.txt"):
        f = open("pal.txt", "r")
        while True:
            line = f.readline()
            if not line:
                break
            num = int(str(line).rstrip())
            result.append(num)
        return result
    f = open("pal.txt", "w")
    i = 1
    order = 1
    while i <= n:
        begin = order
        end = order * 10 - 1
        k = begin
        while k <= end:
            odd = k
            if i > 1:
                odd = int(str(k) + str(k)[:-1][::-1])
            v = odd * odd
            if is_palindrome(str(v)):
                result.append(v)
                f.write(str(v) + '\n')
            k += 1
        k = begin
        while k <= end:
            even = int(str(k) + str(k)[::-1])
            v = even * even
            if is_palindrome(str(v)):
                result.append(v)
                f.write(str(v) + '\n')
            k += 1
        i += 1
        order *= 10
    return result


def solve(a, b, table):
    cnt = 0
    for i in table:
        if i > b:
            break
        elif i < a:
            continue
        else:
            cnt += 1
    return cnt

def gen():
    [a, b] = map(int, str(sys.stdin.readline()).rstrip().split())
    return a, b

def main():
    table = fair_and_square(25)
    tests = int(str(sys.stdin.readline()).rstrip())
    i = 1
    while i <= tests:
        a, b = gen()
        result = solve(a, b, table)
        print 'Case #{0}: {1}'.format(i, result)
        i += 1

if __name__ == "__main__":
    main()
