# -*- coding: utf-8 -*-

def is_sorted(x):
    return sorted(x) == x

def calc(x):
    if is_sorted(x):
        return x

    xlen = len(x)
    fixed = []
    for i, k in enumerate(x):
        if i + 1 == xlen:
            fixed.append(k)
            return fixed
        m = x[i + 1]
        if k <= m:
            fixed.append(k)
        else:
            fixed.append(k - 1)
            for j in range(i + 1, xlen):
                fixed.append(9)
            return calc(fixed)


def solve(x):
    n = [int(j) for j in list(x)]
    max_tidy = calc(n)
    return str(int(''.join([str(o) for o in max_tidy])))


for case in range(1, 1 + int(input())):
    xi = input()
    print('Case #{}: {}'.format(case, solve(xi)))
