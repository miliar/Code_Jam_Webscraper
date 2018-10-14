#!/usr/bin/python3

from sys import argv
# from math import abs

infile = open(argv[1])
cases = int(infile.readline())
for i in range(cases):
    r, c, d = map(int, infile.readline().split())
    w = []
    for j in range(r):
        w.append(list(map(int, infile.readline().rstrip('\n'))))
    # print('W:')
    # for j in range(r):
    #     for k in range(c):
    #         print(w[j][k], end=' ')
    #     print()
    # print('r = {}  c = {}'.format(r, c))
    biggestk = None
    for k in range(min(r,c), 2, -1):
        # print('Trying {}'.format(k))
        for l in range(0, r - k + 1):
            for m in range(0, c - k + 1):
                cx, cy = l + (k - 1) / 2, m + (k - 1) / 2
                mx, my = 0, 0
                # I could try a different order to minimize rounding error
                for x in range(l, l + k):
                    for y in range(m, m + k):
                        if ((x == l or x == l + k - 1) and
                            (y == m or y == m + k - 1)):
                            continue
                        mx += (cx - x) * w[x][y]
                        my += (cy - y) * w[x][y]
                # print('starting at {},{} with k={} c={},{}'.format(l, m, k, mx, my))
                if abs(mx) < 1e-6 and abs(my) < 1e-6:
                    biggestk = k
                    break
            if biggestk is not None:
                break
        if biggestk is not None:
            break
    print('Case #{}: {}'.format(i+1, 'IMPOSSIBLE' if biggestk is None else biggestk))
