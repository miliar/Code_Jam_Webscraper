import argparse
import math
import operator
import sys


def get_max_area(pancakes, count):
    """Get the maximum exposed area."""
    pancakes = [
        (math.pi * r ** 2, math.pi * 2 * r * h)
        for r, h in pancakes
    ]
    pancakes.sort(
        key=operator.itemgetter(1), reverse=True
    )
    return max(
        get_max_from_base(pancakes, count, base_idx)
        for base_idx in range(len(pancakes))
    )


def get_max_from_base(pancakes, count, base_idx):
    """Get the maximum exposed area for given base."""
    base_h, base_v = pancakes[base_idx]
    area = base_h + base_v
    count -= 1

    for i, v in enumerate(pancakes):
        if count == 0:
            break
        if v[0] > base_h or i == base_idx:
            continue
        area += v[1]
        count -= 1
        continue

    return area if count == 0 else 0


def main():
    """The main driver."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'input', type=argparse.FileType('r'), default=sys.stdin
    )
    args = parser.parse_args()
    inp = args.input

    n_tests = int(inp.readline())
    for test_idx in range(n_tests):
        n, k = [int(i) for i in inp.readline().split()]
        pancakes = []
        for _ in range(n):
            pancakes.append(tuple(
                int(i) for i in inp.readline().split()
            ))
        print('Case #{}: {}'.format(test_idx + 1, get_max_area(pancakes, k)))
        continue


if __name__ == '__main__':
    main()
