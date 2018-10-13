#!/usr/bin/env pypy3

def is_tidy_slow(n):
    s = str(n)
    for i in range(len(s) - 1):
        if s[i + 1] < s[i]:
            return False
    return True

def solve_slow(n):
    c = n
    while not is_tidy(c):
        c -= 1
    return c

def is_tidy(s):
    for i in range(len(s) - 1):
        if s[i + 1] < s[i]:
            return False
    return True

def solve(n):
    s = str(n)

    for d in range(0, 19):
        while not is_tidy(s) and s[-d - 1] != '9':
            n -= 10 ** d
            s = str(n)

    return n

def main():
    n_tests = int(input())
    for i in range(n_tests):
        n = int(input())
        print("Case #{}: {}".format(i + 1, solve(n)))

main()
