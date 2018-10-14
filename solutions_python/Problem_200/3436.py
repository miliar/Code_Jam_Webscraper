#!/usr/bin/env python3
import sys

DIGITS = list('0123456789')


def is_tidy(number, backwards=False, ignore_last_digits=0):
    if backwards:
        s = str(number)[::-1]
    else:
        s = str(number)
    last_digit = '0'
    for i in range(len(s) - ignore_last_digits):
        if s[i] < last_digit:
            return False
        last_digit = s[i]
    return True


def previous_tidy(number: int):
    num_len = len(str(number))
    while not is_tidy(number):
        prev_digit = number % 10  # last digit
        for i in range(num_len - 2, -1, -1):
            magnitude = num_len - i - 1
            if prev_digit < number // (10 ** magnitude) % 10:
                # subtract one from that digit and make everything after it 9
                n = list(str(number))
                n[i] = DIGITS[DIGITS.index(n[i]) - 1]  # set n[i] to previous digit
                for j in range(i + 1, len(n)):
                    n[j] = '9'
                number = int(''.join(n))
                break
            prev_digit = number // (10 ** magnitude) % 10
    return number


for case_num in range(int(input())):
    inp = int(input())
    print('performing test case #%d (input=%d)' % (case_num + 1, inp), file=sys.stderr)
    print('Case #%d: %s' % (case_num + 1, previous_tidy(inp)))


if __name__ == '__main__':
    sum([1])
