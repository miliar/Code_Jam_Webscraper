#!/usr/bin/env python

import sys

def baseN(num, base, numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    if num == 0:
        return "0"

    if num < 0:
        return '-' + baseN((-1) * num, base, numerals)

    if not 2 <= base <= len(numerals):
        raise ValueError('Base must be between 2-%d' % len(numerals))

    left_digits = num // base
    if left_digits == 0:
        return numerals[num % base]
    else:
        return baseN(left_digits, base, numerals) + numerals[num % base]

def happysum(number):
    result = 0
    number = str(number)
    for i in number:
        result += int(i)*int(i)
    return result

def ishappy(number, base = 10):
    a = []
    number = baseN(number, base)
    number = str(baseN(int(happysum(number)), base))
    while True:
        number = str(baseN(int(happysum(number)), base))
        if number in a:
            return False
        a.append(number)
        if number == '1':
            return True

def main():
    T = int(raw_input())
    for i in range(T):
        bases = [int(j) for j in raw_input().split()]
        number = 1
        found_happiness = False
        while True:
            number += 1
            if found_happiness:
                break
            for base in bases:
                if not ishappy(number, base):
                    break
                if base == bases[-1]:
                    found_happiness = True
                    print 'Case #%d: %d' % (i+1, number)

if __name__ == '__main__':
    main()

