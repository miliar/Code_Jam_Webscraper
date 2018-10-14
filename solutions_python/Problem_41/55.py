import os
import sys
import re


def read_strs():
    return f.readline().strip().split()


def read_ints():
    return list(map(int, read_strs()))


def solve(n):
    m = {}
    i = len(n) - 1
    m[n[-1]] = i
    while True:
        i -= 1
        if i < 0:
            break
        min = ''
        for x in m:
            if n[i] < x:
                if (not min) or (min > x):
                    min = x
        if not min:
            m[n[i]] = i
        else:
            break
    a = list(n)
    if i == -1:
        num = 0
        idx = len(a) - 1
        while a[idx] == '0':
            num += 1
            idx -= 1
        a = a[: idx + 1]
        a.sort()
        for k in range(num + 1):
            a.insert(1, '0')
    else:
        a[i], a[m[min]] = a[m[min]], a[i]
        b = a[i + 1 :]
        b.sort()
        a = a[: i + 1] + b
    return ''.join(a)
    


# main
with open(sys.argv[1]) as f:
    n = int(f.readline().strip())
    for i in range(1, n + 1):
        t = f.readline().strip()
        print('Case #{}: {}'.format(i, solve(t)))