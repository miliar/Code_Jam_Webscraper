#!/usr/bin/env python3
import sys


def main():
    input_file = sys.argv[1]
    solve(input_file)


def solve(input_file):
    with open(input_file) as f_in:
        t = int(next(f_in))
        for case in range(t):
            n = int(next(f_in))
            mushrooms = tuple(int(num) for num in next(f_in).split())
            min1, min2 = solve_instance(n, mushrooms)
            print("Case #%d: %d %d" % (case + 1, min1, min2))


def solve_instance(n, mushrooms):
    return solve1(n, mushrooms), solve2(n, mushrooms)


def solve1(_, mushrooms):
    return sum(
        max(mprev - mnext, 0)
        for mprev, mnext in zip(mushrooms, mushrooms[1:])
    )


def solve2(_, mushrooms):
    consumption = max(
        mprev - mnext
        for mprev, mnext in zip(mushrooms, mushrooms[1:])
    )
    consumption = max(0, consumption)

    return sum(
        min(consumption, m)
        for m in mushrooms[:-1]
    )


if __name__ == '__main__':
    main()
