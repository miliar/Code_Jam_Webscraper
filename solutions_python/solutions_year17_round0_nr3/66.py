#!/usr/bin/env python


def solve(N, K):
    space = {N: 1}

    while True:
        largest = max(space)
        count = space.pop(largest)

        z = (largest-1) // 2
        y = largest - 1 - z

        K -= count
        if K <= 0:
            return y, z

        if y > 0:
            space[y] = space.get(y, 0) + count
        if z > 0:
            space[z] = space.get(z, 0) + count


def main():
    N = int(raw_input())
    for case in xrange(N):
        N, K = map(int, raw_input().split())
        y, z = solve(N, K)
        print "Case #{}: {} {}".format(case+1, y, z)


if __name__ == '__main__':
    main()
