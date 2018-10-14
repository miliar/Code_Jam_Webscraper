# coding: utf-8

import sys
import itertools

def is_palindrome(n):
    s = str(n)
    return list(s) == list(reversed(s))

def calc(a, b):
    ans = 0
    for i in itertools.count(1):
        n = i * i
        if n > b: break

        if is_palindrome(i) and is_palindrome(n) and (a <= n <= b):
            # print(i, n)
            ans += 1
    return ans

def main():
    n = int(sys.stdin.readline())

    for cc in range(n):
        a, b = map(int, sys.stdin.readline().split())
        print("Case #%d: %d" % (cc+1, calc(a, b)))

if __name__ == "__main__":
    main()
