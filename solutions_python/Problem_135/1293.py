#!/usr/bin/env python
import sys


def problem(fi):
    r1 = int(fi.readline().strip())
    arr1 = []
    for i in range(4):
        arr1.append([int(c) for c in fi.readline().strip().split(' ')])
    r2 = int(fi.readline().strip())
    arr2 = []
    for i in range(4):
        arr2.append([int(c) for c in fi.readline().strip().split(' ')])
    return r1, arr1, r2, arr2


def solve(params, fo, i):
    r1, arr1, r2, arr2 = params
    cards1 = set(arr1[r1 - 1])
    cards2 = set(arr2[r2 - 1])
    cards = cards1 & cards2
    if not cards:
        return 'Volunteer cheated!'
    elif len(cards) > 1:
        return 'Bad magician!'
    else:
        return cards.pop()


if __name__ == '__main__':
    with open(sys.argv[1]) as fi, open(sys.argv[2], 'w') as fo:
        total = int(fi.readline().strip())
        for i in range(total):
            res = solve(problem(fi), fo, i)
            fo.write('Case #{0}: {1}\n'.format(i + 1, res))
            fo.flush()
