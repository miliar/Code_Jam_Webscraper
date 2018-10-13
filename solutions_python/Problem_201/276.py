import os
import sys


def next(n, res):
    parts = (n, n+1)
    num = (1, 0)

    while True:
        # print(parts, num)
        new_parts = (0, 0)
        new_num = (0, 0)
        a, b = num
        if b >= res:
            return parts[1] // 2, (parts[1]-1) // 2
        res -= b
        if a >= res:
            return parts[0] // 2, (parts[0]-1) // 2
        res -= a
        if parts[0] % 2 == 0:
            new_num = (a, a + 2*b)
            new_parts = (parts[0] // 2 - 1, parts[0] // 2)
        else:
            new_num = (a*2 + b, b)
            new_parts = (parts[0] // 2, parts[0] // 2 + 1)
        parts = new_parts
        num = new_num


def calc(x):
    n, k = x.split(' ')
    n = int(n)
    k = int(k)
    return next(n, k)


if __name__ == "__main__":
    with open('C-large.in', 'r') as f:
        n = int(f.readline())
        for i in range(n):
            l, r = calc(f.readline().strip())
            print("Case #%d: %d %d" % (i+1, l, r))
