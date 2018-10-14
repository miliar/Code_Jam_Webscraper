#!/usr/bin/env python3
import sys


def main():
    input_file = sys.argv[1]
    solve(input_file)


def solve(input_file):
    with open(input_file) as f_in:
        next(f_in)
        for i, input_line in enumerate(f_in):
            N = int(input_line)
            max_tidy = solve_instance(N)
            print("Case #%d: %d" % (i + 1, max_tidy))


def solve_instance(N):
    digits = str(N)
    pieces = max_tidy(digits)
    return int(''.join(pieces).lstrip('0'))


def max_tidy(digits):
    for i, (cur, prev) in enumerate(zip(digits[1:], digits)):
        if cur < prev:
            partial_sol = max_tidy(str(-1 + from_digits(digits[:i+1])))
            partial_sol.append('9' * (len(digits) - i - 1))
            return partial_sol

    return [digits]


def from_digits(digits):
    if not digits:
        return 0
    return int(''.join(digits))


if __name__ == '__main__':
    main()
