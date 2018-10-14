#!/usr/bin/env python
# -*- coding: utf-8 -*-

def calculate(X, R, C):
    winner = 'RICHARD'

    if X == 1:
        return 'GABRIEL'

    if (R * C) % X == 0 and X <= max([R, C]):
        winner = 'GABRIEL'

    if (X / 2) >= min([R, C]) and X > 2:
        winner = 'RICHARD'

    return winner

def main():
    with open('D-small-attempt3.in') as f:
        data = f.read().strip().split('\n')

    TEST_CASES = None
    RESULTS = []
    D = None
    P = None
    case = 1
    for c, row in enumerate(data):
        if c == 0:
            TEST_CASES = int(row)
            continue

        X, R, C = map(int, row.split(' '))
        winner = calculate(X, R, C)
        result = 'Case #'+str(c)+': '+winner
        RESULTS.append(result)

    with open('D-small-attempt3.out', 'w') as f:
        f.write('\n'.join(RESULTS))

if __name__ == '__main__':
    main()
