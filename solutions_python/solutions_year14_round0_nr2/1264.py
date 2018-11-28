#!/usr/bin/env python
import sys


def problem(fi):
    return [float(f) for f in fi.readline().strip().split(' ')]


def solve(params, fo, i):
    c, f, x = params
    v = 2.0
    tmin = x / v
    cur_v = v
    buy_time = 0.0
    while True:
        buy_time = buy_time + c / (cur_v)
        t = buy_time + x / (cur_v + f)
        if (t < tmin):
            tmin = t
            cur_v += f
        else:
            break
    return tmin


if __name__ == '__main__':
    with open(sys.argv[1]) as fi, open(sys.argv[2], 'w') as fo:
        total = int(fi.readline().strip())
        for i in range(total):
            res = solve(problem(fi), fo, i)
            fo.write('Case #{0}: {1:.7f}\n'.format(i + 1, res))
            fo.flush()
