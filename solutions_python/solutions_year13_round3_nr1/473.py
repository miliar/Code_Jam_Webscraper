# -*- coding: utf-8 -*-

from sys import exit, stdin
from pprint import PrettyPrinter
from re import finditer


if __name__ == '__main__':
    vowels = 'aeiou'

    p = PrettyPrinter()

    T = int(stdin.readline())

    for index in range(T):
        name, n = stdin.readline().strip().split()
        n = int(n)

        name = [
            c if c in vowels else '1'
            for c in name
        ]
        name = ''.join(name)

        def all_chains():
            for start in range(len(name) + 1):
                for end in range(len(name) + 1):
                    if end - start >= n:
                        yield name[start:end]
            yield ''

        count = 0

        for _ in all_chains():
            if _:
                if '1' * n in _:
                    count += 1

        print 'Case #%d: %d' % (index + 1, count)

    exit()
