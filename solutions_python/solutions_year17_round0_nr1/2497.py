from __future__ import print_function
from sys import argv
from sys import stdout
from math import ceil


def memoizing(func):
    """Function decorator to cache a function's output."""
    memos = dict()

    def memoize(*args):
        if args in memos:
            return memos[args]
        res = func(*args)
        memos[args] = res
        return res
    return memoize


def helper(minutes):

    i = 0
    x = ceil(float(minutes) / 2.0)
    while x+i < minutes :
        x = ceil(float(minutes) / 2.0)
        i += 1


def solve(S, K):
    """write your code here"""
    sl = [True if c == '+' else False for c in S]
    flips = 0
    i = 0
    while i <= len(sl) - K:
        if not sl[i]:
            for c in range(i, i+K):
                sl[c] = not sl[c]
            flips += 1
        i += 1
    return "IMPOSSIBLE" if False in sl[-K:] else flips


def get_input_data(f):
    """write your per case parsing code here"""
    x = read_strings(f)
    return x[0], int(x[1])


def handle_case(case_num, result, output=stdout):
    print("Case #{}: {}".format(case_num, result), file=output)


def main(filename):
    with open(filename) as f:
        for case in range(1, read_int(f) + 1):
            handle_case(case, solve(*get_input_data(f)))


def read_string(f):
    return f.readline().strip()


def read_strings(f, split=' '):
    return [x for x in read_string(f).split(split) if x]


def read_int(f):
    return read_number(f, int)


def read_ints(f):
    return read_numbers(f, int)


def read_float(f):
    return read_number(f, float)


def read_floats(f):
    return read_numbers(f, float)


def read_number(f, type):
    return type(read_string(f))


def read_numbers(f, type):
    return tuple(type(x) for x in read_strings(f))


def get_n_n_matrix(n):
    return get_n_m_matrix(n, n)


def get_n_m_matrix(x, y):
    return [[0 for _ in range(x)] for _ in range(y)]


if __name__ == '__main__':
    if len(argv) < 2:
        print("No input file")
        exit(1)
    main(argv[1])
