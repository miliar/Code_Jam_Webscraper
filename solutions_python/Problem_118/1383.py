#!/usr/bin/env python3
from itertools import combinations
import sys


def palyndromes(length: int) -> int:
    if length == 1:
        for val in [1, 2, 3]:
            yield val
    elif length == 2:
        yield 11
        yield 22
    elif length % 2 == 1:
        if length < 10:
            yield int('1' * length)
    else:
        gen_len = length // 2 - 1
        for i in range(min(gen_len + 1, 4)):
            for comb in combinations(range(gen_len), i):
                s = ['0'] * gen_len
                for index in comb:
                    s[index] = '1'
                yield int('1' + ''.join(s) + ''.join(reversed(s)) + '1')
        yield int('2' + '0' * (length - 2) + '2')
    return


def is_palyndrome(val: int) -> bool:
    return str(val) == str(val)[::-1]


def solve(data):
    A, B = data
    result = 0
    for i in range(1, 50):
        for val in palyndromes(i):
            val_sq = val ** 2
            if val_sq > B:
                return result
            if A <= val_sq and is_palyndrome(val_sq):
                # print('{:<12} - {}'.format(val, val_sq))
                result += 1
    return result


def read(fin):
    return map(int, fin.readline().split())


def main():
    try:
        fin = open(sys.argv[1])
        if len(sys.argv) >= 3:
            fout = open(sys.argv[2], 'w')
        else:
            fout = sys.stdout
    except IndexError:
        print('Not enough command line options')
        sys.exit(1)
    except IOError as e:
        print(e)
        sys.exit(2)

    T = int(fin.readline())
    for t in range(T):
        data = read(fin)
        print('Case #{}: {}'.format(t + 1, solve(data)), file=fout)


if __name__ == '__main__':
    main()
