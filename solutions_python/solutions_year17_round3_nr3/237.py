#!/usr/bin/env python
import sys


def problem(fi):
    n, k = fi.readline().strip().split(' ')
    u = fi.readline().strip()
    ps = [float(p) for p in fi.readline().strip().split(' ')]
    return int(n), int(k), float(u), ps


def success(batches):
    success_p = 1.0
    for p, count in reversed(batches):
        success_p *= (p ** count)
    return success_p


def solve(params, i):
    n, k, u, ps = params

    assert n == k

    batches = [[1.0, 0]]
    for p in sorted(ps, reverse=True):
        if not batches:
            batches.append([p, 1])
        else:
            if batches[-1][0] - p < 0.00000001:
                batches[-1][1] += 1
            else:
                batches.append([p, 1])

    while u > 0.00000001:
        cur_p, cur_count = batches[-1]
        next_p, next_count = batches[-2]
        p_diff = next_p - cur_p
        u_split = min(u, p_diff * cur_count)

        p_inc = u_split / cur_count

        batches[-1][0] += p_inc
        if next_p - batches[-1][0] < 0.00000001:
            batches.pop()
            batches[-1][1] += cur_count

        u -= u_split

    success_p = success(batches)

    return '{:.6f}'.format(success_p)


if __name__ == '__main__':
    with open(sys.argv[1]) as fi, open(sys.argv[2], 'w') as fo:
        total = int(fi.readline().strip())
        for i in range(total):
            print 'Case #{0} solved'.format(i + 1)
            res = solve(problem(fi), i)
            fo.write('Case #{0}: {1}\n'.format(i + 1, res))
            fo.flush()
