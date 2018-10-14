#! /usr/bin/env python

import math

def palindrome(n):
    return str(n) == str(n)[::-1]

def fairandsquare(lower, upper):
    count = 0
    i = int(math.ceil(math.sqrt(lower)))
    while i**2 <= upper:
        if palindrome(i) and palindrome(i**2) and lower <= i**2 <= upper:
            count += 1
        i += 1
    return count

def main():
    n = int(raw_input())

    for i in range(n):
        lower, upper = map(int, raw_input().split(' '))
        print 'Case #%d: %d' % (i+1, fairandsquare(lower, upper))

if __name__ == '__main__':
    main()
