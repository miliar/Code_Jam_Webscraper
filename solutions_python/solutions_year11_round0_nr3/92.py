import sys
import functools

def read_case(lines):
    n = int(lines.next())
    arr = [int(i) for i in lines.next().split()]
    return arr


def read_input(path):
    cases = []
    with file(path) as f:
        lines = iter(f)
        n = int(lines.next())

        for i in range(1, 1 + n):
            cases.append((i, read_case(lines)))

    return cases


def solve(arr):
    x = 0
    for i in arr:
        x ^= i

    if x != 0:
        return 'NO'

    return sum(arr) - min(arr)


if __name__ == '__main__':
    cases = read_input(sys.argv[1])
    for i, case in cases:
        print 'Case #%d: %s' % (i, solve(case))
