#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Problem A. Getting the Digits
# https://code.google.com/codejam/contest/11254486/dashboard#s=p0
#

import sys
import random

DIGITS = ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE")


def solve(S):
    phone = []
    chars = {}
    for c in S:
        chars[c] = chars.get(c, 0) + 1

    def xxx(digit, count):
        for index in range(count):
            phone.append(digit)
            for letter in DIGITS[digit]:
                chars[letter] -= 1

    xxx(0, chars.get('Z', 0))
    xxx(2, chars.get('W', 0))
    xxx(4, chars.get('U', 0))
    xxx(6, chars.get('X', 0))
    xxx(8, chars.get('G', 0))
    xxx(7, chars.get('S', 0))
    xxx(5, chars.get('V', 0))
    xxx(3, chars.get('R', 0))
    xxx(9, chars.get('I', 0))
    xxx(1, chars.get('O', 0))

    return ''.join(str(digit) for digit in sorted(phone))


def main(IN, OUT):
    T = int(IN.readline())
    for index in range(T):
        S = IN.readline().strip()
        OUT.write('Case #{}: {}\n'.format(index + 1, solve(S)))


def makesample(T=100, maxlength=2000):
    print(T)
    for n in range(T):
        S, challenge = '', ''
        while len(S + challenge) <= maxlength:
            S += challenge
            challenge = random.choice(DIGITS)
        S = list(S)
        random.shuffle(S)
        print(''.join(S))


if __name__ == '__main__':
    if '-makesample' in sys.argv[1:]:
        makesample()
    else:
        main(sys.stdin, sys.stdout)
