import StringIO

import itertools

from ecodejam.input_parser import *


def is_tidy(i):
    return sorted(map(int, str(i))) == map(int, str(i))


def solve_naive(case_index):
    print case_index
    n = read_int()
    next_line()

    for i in xrange(n, -1, -1):
        if is_tidy(i):
            return str(i)


def solve_fast(case_index):
    print case_index
    n = read_int()
    next_line()

    while not is_tidy(n):
        digits = map(int, str(n))[::-1]
        for i in xrange(0, len(digits) - 1):
            if digits[i] < digits[i+1]:
                n = int("0" + str(n)[:-(i + 1)], 10)
                n -= 1
                n = str(n) + "9" * (i + 1)
                n = int(n, 10)
                break

    return str(n)


solve = solve_fast

SAMPLE = """
4
132
1000
7
111111111111111110"""

if __name__ == "__main__":
    set_parsed_input(
        StringIO.StringIO(SAMPLE)
    )
    run_solver(solve)
