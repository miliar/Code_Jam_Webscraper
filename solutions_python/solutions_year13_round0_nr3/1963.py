import sys
import itertools


def is_pal(n):
    return str(n) == str(n)[::-1]


def fair_squares(a, b):
    c = 0
    start = int(a ** .5) - 1
    for i in itertools.count(start):
        if i ** 2 > b:
            return c
        if is_pal(i) and is_pal(i ** 2) and i ** 2 >= a:
            c += 1


if __name__ == '__main__':
    with open(sys.argv[2], 'w') as out:
        with open(sys.argv[1]) as in_:
            next(in_)
            for i, test in enumerate(in_, 1):
                out.write('Case #{}: {}\n'.format(i, fair_squares(*map(int,
                                                                     test.strip().split()))))
