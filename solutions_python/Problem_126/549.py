import sys
from itertools import imap

from utils import stripped_lines


VOWELS = {'a', 'e', 'i', 'o', 'u'}


def consecutive_groups(iterable):
    s = tuple(iterable)
    for size in range(1, len(s) + 1):
        for index in range(len(s) + 1 - size):
            yield iterable[index:index + size]


def quantify(iterable, pred=bool):
    "Count how many times the predicate is true"
    return sum(imap(pred, iterable))


def predicate(n):
    def f(substring):
        count = 0
        for char in substring:
            if char not in VOWELS:
                count += 1
            else:
                count = 0
            if count >= n:
                return True
        return False
    return f


def solve(word, n):
    return quantify(consecutive_groups(word), predicate(n))


def main():
    lines = stripped_lines(sys.stdin)
    numcases = int(lines.next())

    for i in range(numcases):
        word, n = lines.next().split()
        n = int(n)

        result = solve(word, n)

        print 'Case #%d: %s' % (i + 1, result)

if __name__ == '__main__':
    main()
