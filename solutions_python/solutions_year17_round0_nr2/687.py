"""
Code Jam 2017
Qualification Round
Problem B - Tidy Numbers

Author: Ben Feinstein
"""
from __future__ import print_function, division


def largest_tidy(n):
    digits = [int(d) for d in str(n)]
    # can be computed faster, but it's unnecessary for less than 18 digits
    last_digit = -1
    result = 0
    is_smaller = False
    for i, digit in enumerate(digits):
        if is_smaller:
            result = 10 * result + 9
        elif digit < last_digit:
            is_smaller = True
            result = largest_tidy(result - 1)
            result = 10 * result + 9
        else:
            result = result * 10 + digit
        last_digit = digit

    return result


def is_tidy(n):
    s = str(n)
    ld = '0'
    for d in s:
        if d < ld:
            return False
        ld = d
    return True


def largest_tidy_naive(n):
    m = 0
    for i in range(0, n + 1):
        if is_tidy(i):
            m = i

    return m


def main():
    n_tests = int(input())
    for test_case in range(1, n_tests + 1):
        n = int(input())
        tidy = largest_tidy(n)
        # naive_tidy = largest_tidy_naive(n)
        # assert tidy == naive_tidy, "%d %d %d" % (n, tidy, naive_tidy)
        print("Case #{test_case:d}: {tidy:d}".format(test_case=test_case, tidy=tidy))


if __name__ == '__main__':
    main()
