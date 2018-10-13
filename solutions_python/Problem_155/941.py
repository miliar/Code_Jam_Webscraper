# coding: utf-8

import sys

filename = 'sample.txt' if len(sys.argv) == 1 else sys.argv[1]
with open(filename, 'r', encoding = 'shift_jis') as f:
    T = int(f.readline()[:-1])
    for t in range(T):
        Smsx, Si = f.readline()[:-1].split()

        level = 0
        count = 0
        result = 0
        for s in Si:
            if (s != '0' and count < level):
                result += level - count
                count += level - count

            count += int(s)
            level += 1

        print('Case #{0}: {1}'.format(t + 1, result))
