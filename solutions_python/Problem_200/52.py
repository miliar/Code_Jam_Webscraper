import sys
import codejam


def is_tidy(n):
    return str(n) == ''.join(sorted(str(n)))


def expand_trailing_nine(n):
    if n < 10:
        return n
    if n % 10 == 9:
        return expand_trailing_nine(n // 10) * 10 + 9
    return n - (n % 10 + 1)


def last_tidy_number(n):
    while not is_tidy(n):
        n = expand_trailing_nine(n)
    return n


def parser(reader):
    n = int(reader.readline())
    return last_tidy_number(n)


if __name__ == '__main__':
    codejam.run(parser, open('tidy-large.in', 'r'), open('tidy-large.out', 'w'))
