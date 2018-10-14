#!/usr/bin/env python3
# coding: utf-8

def f():
    a = int(input())

    for i in range(4):
        line = input()
        if i + 1 == a:
            ret = set(line.split(' '))

    return ret

def solve(a, b):
    cands = a & b
    n = len(cands)

    if n == 0:
        return 'Volunteer cheated!'
    elif n == 1:
        return list(cands)[0]
    else:
        return 'Bad magician!'

for case in range(int(input())):
    a = f()
    b = f()

    print('Case #{}: {}'.format(case + 1, solve(a, b)))
