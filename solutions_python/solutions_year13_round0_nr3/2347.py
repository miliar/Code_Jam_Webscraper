#!/usr/bin/env python
import sys
from math import sqrt

def is_palindrome(n):
    '''
    Check if a number is palindromic.

    '''
    return str(n) == ''.join(reversed(str(n)))


def generate_palindromes(start, stop):
    '''
    Generate palindrome numbers in the closed range [start, stop].

    '''
    current = start
    while current <= stop:
        if is_palindrome(current):
            yield current
        current += 1


def is_square(n):
    if n in (0, 1):
        return True
    x = n / 2
    seen = {x}
    while x * x != n:
        x = (x + n / x) / 2
        if x in seen:
            return False
        seen.add(x)
    return True


if __name__ == '__main__':
    t = int(sys.stdin.readline())
    for i in xrange(t):
        a, b = map(int, sys.stdin.readline().split())
        count = 0
        for pal in generate_palindromes(a, b):
            if is_square(pal) and is_palindrome(int(sqrt(pal))):
                count += 1
        sys.stdout.write('Case #{}: {}\n'.format(i + 1, count))


