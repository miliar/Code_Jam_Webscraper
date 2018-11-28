"""
Google Code Jam
2017 Qualification Round

Problem B. Tidy Numbers
    :author: yamaton
    :date: 2017-04-08
"""
import functools
import itertools as it
import sys


def integerdigits(n):
    """Construct list of decimal digits from the integer n

    >>> integerdigits(235)
    [2, 3, 5]
    """
    return [int(i) for i in str(n)]


def fromdigits(xs):
    """Constructs an integer from the list of decimal digits.

    >>> fromdigits([1, 9, 4, 2])
    1942
    """
    return functools.reduce(lambda i, j: 10 * i + j, xs, 0)


def is_tidy(xs):
    return all(map(lambda tup: tup[0] <= tup[1], zip(xs, xs[1:])))


def solve(n):
    xs = integerdigits(n)
    if is_tidy(xs):
        return n

    ptr = sum(1 for _ in it.takewhile(lambda tup: tup[0] < tup[1], zip(xs, xs[1:])))
    k = xs[ptr] - 1
    padlen = len(xs) - ptr - 1
    pp(ptr, k)
    ys = xs[:ptr] + [k] + [9] * padlen
    res = fromdigits(ys)
    return res


def pp(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    for _tc in range(1, int(input())+1):
        pp('\n--------- case #%d -------' % _tc)
        print("Case #%d: " % _tc, end='')
        n = int(input())

        result = solve(n)
        pp()
        pp('n      =', n)
        pp('result =', result)
        print(result)




if __name__ == '__main__':
    main()
