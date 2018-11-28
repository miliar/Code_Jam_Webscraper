#!/usr/bin/env python3
import sys

__author__ = 'timofey'


def solve(handle):
    row1 = int(handle.readline())
    rows1 = [set(handle.readline().split()) for _ in range(4)]
    selection1 = rows1[row1 - 1]
    row2 = int(handle.readline())
    rows2 = [set(handle.readline().split()) for _ in range(4)]
    selection2 = rows2[row2 - 1]
    result = selection1.intersection(selection2)
    if len(result) == 1:
        return next(iter(result))
    elif len(result) > 1:
        return 'Bad magician!'
    else:
        return 'Volunteer cheated!'


def main(handle):
    count = int(handle.readline())
    for i in range(count):
        print('Case #{}: {}'.format(i+1, solve(handle)))


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as handle:
        main(handle)
