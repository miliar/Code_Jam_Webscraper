# -*- coding: utf-8 -*-
from math import pow


def isPalindrome(s):
    return s == s[::-1]

with open('C-small-attempt0.in', 'r') as input:
    with open('C-small-attempt0.out', 'w') as output:
        T = int(input.readline())

        for index in range(1, T + 1):
            A, B = map(int, input.readline().split())
            count = 0

            for i in xrange(A, B + 1):
                p = str(i)
                _sp = pow(i, 0.5)
                if int(_sp) * 1.0 != _sp:
                    continue
                sp = str(int(_sp))

                if isPalindrome(p) and isPalindrome(sp):
                    count += 1

            output.write('Case #%i: %s\n' % (index, count))
