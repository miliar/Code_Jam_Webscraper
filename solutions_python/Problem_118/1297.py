import itertools
import sys
import math


def get_num_fair_and_squared_in_intervals(ranges):
    r = list(ranges)
    max_digits = int(math.log10(math.sqrt(max(r, key=lambda x: x[1])[1]))) + 1

    fair_and_squared = list(get_fair_and_squared_numbers(max_digits))

    return [len([x for x in fair_and_squared if a <= x <= b]) for (a, b) in r]


def get_fair_and_squared_numbers(max_digits):
    for digits in range(1, max_digits+1):
        for p in palindromes(digits):
            psquared = p**2
            if is_palindrome(str(psquared)):
                yield psquared


def palindromes(n):
    if n == 1:
        for i in range(10):
            yield i
    elif n == 2:
        for i in range(1, 10):
            yield 10 * i + i
    else:
        for x in palindromes(n-2):
            for i in range(1, 10):
                yield 10**(n-1) * i + 10 * x + i


def is_palindrome(x):
    return x[::-1] == x


def read_input(path):
    with open(path) as f:
        lineiterator = iter(f)

        num_intervals = int(next(lineiterator))

        for i in range(num_intervals):
            yield list(map(int, next(lineiterator).split()))


def write_solutions(path, solutions):
    with open(path, "w") as f:
        for i, solution in zip(itertools.count(1), solutions):
            print("Case #{num}: {value}".format(num=i, value=str(solution)), file=f)


if __name__ == '__main__':
    intervals = read_input(sys.argv[1])
    num_fair_and_squared_in_intervals = get_num_fair_and_squared_in_intervals(intervals)
    write_solutions(sys.argv[2], num_fair_and_squared_in_intervals)

