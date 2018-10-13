#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_array(lig, col):
    a = []
    for n in range(lig):
        a.append([int(_) for _ in input().strip().split(' ')])
    return a
    
def test(a, lig, col):
    mlig = [max(a[i][k] for k in range(col)) for i in range(lig)]
    mcol = [max(a[k][j] for k in range(lig)) for j in range(col)]
    for i, l in enumerate(a):
        for j, v in enumerate(l):
            if v < mlig[i] and v < mcol[j]:
                return 'NO'
    return 'YES'

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        lig, col = [int(_) for _ in input().strip().split(' ')]
        a = get_array(lig, col)
        print('Case #{}: {}'.format(i + 1, test(a, lig, col)))
