import functools
import time
import bisect

import sys


@functools.lru_cache(maxsize=int(2E6))
def gen_all_tidy(start, length):
    if length == 1:
        return list(range(start, 10))
    else:
        new_list = []
        for fst in range(start, 10):
            rest = gen_all_tidy(fst, length - 1)
            for number in rest:
                new_list.append(int(str(fst) + str(number)))
        return new_list


@functools.lru_cache(100)
def get_all_length_tidy(length):
    all_tidy = []
    for l in range(1, length + 1):
        all_tidy += gen_all_tidy(1, l)
    return all_tidy


def test_it():
    print(gen_all_tidy(3, 1))
    print(gen_all_tidy(9, 4))
    print(gen_all_tidy(8, 3))
    print(gen_all_tidy(1, 3))

    t0 = time.time()
    print(len(gen_all_tidy(1, 18)))
    print("Czas", time.time() - t0)

    t0 = time.time()
    print(len(gen_all_tidy(1, 18)))
    print("Czas", time.time() - t0)


def solve(n):
    all_tidy = get_all_length_tidy(18)
    i = bisect.bisect_right(all_tidy, n)
    return all_tidy[i - 1]


def test_case(n, exp):
    assert solve(n) == exp
    print("OK")


def all_tests():
    test_case(132, 129)
    test_case(1000, 999)
    test_case(7, 7)
    test_case(111111111111111110, 99999999999999999)


def gi():
    return int(sys.stdin.readline().strip())


def solve_codejam():
    n = gi()
    for test_nr in range(1, n + 1):
        print("Case #%d: %d" % (test_nr, solve(gi())))

solve_codejam()
