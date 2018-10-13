#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(cipher):
    num = cipher
    prev_digit = None
    i = len(num)-1
    while i != -1:
        digit = num[i]
        j = len(num)-i-1
        if prev_digit:
            if digit > prev_digit:
                offset = 0
                carry_fix = ''
                if prev_digit == '0':
                    new_digit = str(int(digit)-1)
                    if new_digit == '-1':
                        new_digit = '9'
                        if i != 0:
                            offset = -1
                            carry_fix = str(int(num[i+offset])-1)
                            if carry_fix == '-1':
                                carry_fix = '9'
                elif digit == '1':
                    new_digit = ''
                else:
                    new_digit = str(int(digit)-1)
                if i == 0 and new_digit == '0':
                    new_digit = ''
                num = num[:i+offset] + carry_fix + new_digit + '9'*(len(num)-(i+1))
        prev_digit = num[i]
        i -= 1
    return num

if __name__ == "__main__":
    testcases = input()

    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))
