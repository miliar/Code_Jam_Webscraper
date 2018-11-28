import sys
import functools

def read_case(lines):
    n = int(lines.next())
    arr = [int(i) for i in lines.next().split()]
    return (n, arr)


def read_input(path):
    cases = []
    with file(path) as f:
        lines = iter(f)
        n = int(lines.next())

        for i in range(1, 1 + n):
            cases.append((i, read_case(lines)))

    return cases


def solve(case):
    n, arr = case

    in_place = len([x for i,x in enumerate(arr) if x == i + 1])
    return n - in_place

if __name__ == '__main__':
    cases = read_input(sys.argv[1])
    for i, case in cases:
        print 'Case #%d: %d' % (i, solve(case))
