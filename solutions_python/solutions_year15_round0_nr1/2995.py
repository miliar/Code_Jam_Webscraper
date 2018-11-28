import sys


def solve(case):
    s = 0
    r = 0
    for i, v in enumerate(case, 1):
        s += int(v)
        if s < i:
            r += i - s
            s = i
    return r

if __name__ == '__main__':
    N = int(next(sys.stdin))
    for i in range(1, N + 1):
        print('Case #{}: {}'.format(i,
                                    solve(next(sys.stdin).rsplit(maxsplit=1)[1])))
