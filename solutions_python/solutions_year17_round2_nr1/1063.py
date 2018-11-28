from __future__ import print_function
from sys import argv
from sys import stdout
from collections import Counter


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


def helper_func(*args):
    """global helper function"""
    return


def optimized(*args):
    """optimized solution"""
    return None


def naive(*args):
    """naive solution"""
    D, N, H = args
    H.sort(reverse=True)

    min_time = 0
    for prev_D, prev_S in H:
        min_time = max((D - prev_D) / prev_S, min_time)

    return D/min_time


def solve(*args):
    """returns the best solution available"""
    return optimized(*args) or naive(*args)


def get_input_data(f):
    """write your per case parsing code here"""
    D, N = read_ints(f)
    return D, N, [read_floats(f) for _ in range(N)]



def handle_case(case_num, result, output=stdout):
    """outputs case result(s)"""
    print("Case #{}: {}".format(case_num, result), file=output)


def main(filename):
    """reads test cases and outputs the result(s)"""
    with open(filename) as f:
        for case in range(1, read_int(f) + 1):
            handle_case(case, solve(*get_input_data(f)))


"""BEGIN: Helper functions"""


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


"""END: Helper functions
   BEGIN: ENTRY"""

if __name__ == '__main__':
    if len(argv) < 2:
        print("No input file")
        exit(1)
    main(argv[1])

"""END: ENTRY"""
