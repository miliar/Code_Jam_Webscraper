# coding: utf-8

import sys

filename = 'sample.txt' if len(sys.argv) == 1 else sys.argv[1]
with open(filename, 'r', encoding = 'shift_jis') as f:
    T = int(f.readline()[:-1])
    for i in range(T):
        X, R, C = [int(s) for s in f.readline()[:-1].split()]

        if (R * C) % X != 0:
            print('Case #{0}: {1}'.format(i + 1, 'RICHARD'))
            continue

        if (R * C) < X:
            print('Case #{0}: {1}'.format(i + 1, 'RICHARD'))
            continue

        if R == 1 or C == 1:
            if 3 <= X:
                print('Case #{0}: {1}'.format(i + 1, 'RICHARD'))
                continue

        if max(R, C) == 2:
            if 3 <= X:
                print('Case #{0}: {1}'.format(i + 1, 'RICHARD'))
                continue

        if max(R, C) == 3:
            if X == 4:
                print('Case #{0}: {1}'.format(i + 1, 'RICHARD'))
                continue

        if (R == 4 and C == 2) or (R == 2 and C == 4):
            if X == 4:
                print('Case #{0}: {1}'.format(i + 1, 'RICHARD'))
                continue

        print('Case #{0}: {1}'.format(i + 1, 'GABRIEL'))
