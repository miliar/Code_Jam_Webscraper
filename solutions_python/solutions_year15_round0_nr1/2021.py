#!/usr/bin/env python3

import fileinput


def solve(people):
    people = enumerate(people)
    c = next(people)[1]
    f = 0

    for i, p in people:
        if p == 0:
            continue

        diff = i - c
        c += p

        if diff > 0:
            f += diff
            c += diff

    return f


if __name__ == "__main__":
    lines = (x.strip().split() for x in fileinput.input())

    n = int(next(lines)[0])

    for i, line in enumerate(lines):
        m = int(line[0])
        p = map(int, list(line[1]))

        print('Case #{}: {}'.format(i+1, solve(p)))
