import numpy as np


def calc_area(rhs):
    res = rhs[-1][0] ** 2
    for r, h in rhs:
        res += 2 * h * r
    return res


def find_min(rhs, mp):
    mm, idx = 0, -1
    for i in range(len(rhs) - 1):
        tmp = mp - 2 * rhs[i][0] * rhs[i][1]
        if tmp > mm:
            mm, idx = tmp, i
    r, h = rhs[-1]
    tmp = mp - 2 * h * r - (r**2 - rhs[-2][0]**2)
    if tmp > mm:
        mm, idx = tmp, len(rhs) - 1
    return mm, idx


def main():
    t = int(input())
    for case in range(1, t + 1):
        n, k = map(int, input().split())
        rhs = []
        for _ in range(n):
            r, h = map(int, input().split())
            rhs += [(r, h)]
        rhs = sorted(rhs)
        mp = calc_area(rhs)

        for _ in range(n - k):
            mm, idx = find_min(rhs, mp)
            rhs.pop(idx)
            mp = mm

        print('Case #{}: {}'.format(case, mp * np.pi))

if __name__ == '__main__':
    main()
