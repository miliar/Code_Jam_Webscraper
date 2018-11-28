#!/usr/bin/env python
# -*- coding: utf-8 -*-

def calculate(Smax, Svector):
    Smax = int(Smax)

    if Smax == 0:
        return 0

    Svector = list(map(int, list(Svector)))

    friends = 0
    standing = 0
    for c, x in enumerate(Svector):
        added = 0
        if x > 0 and standing < c:
            added = c - standing
            friends += added
        standing += x + added
        if standing >= Smax:
            break

    return friends

def main():
    with open('A-large.in') as f:
        data = f.read().strip().split('\n')

    TEST_CASES = None
    RESULTS = []
    for c, row in enumerate(data):
        if c == 0:
            TEST_CASES = int(row)
            continue

        Smax, S = row.split(' ')
        Svector = list(S)
        R = calculate(Smax, Svector)
        result = 'Case #'+str(c)+': '+str(R)
        RESULTS.append(result)

    with open('A-large.out', 'w') as f:
        f.write('\n'.join(RESULTS))

if __name__ == '__main__':
    main()
