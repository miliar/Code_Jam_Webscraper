#!/usr/bin/python3
# -*- coding: utf-8 -*-

def possible(i, j):
    p = str(i)
    q = str(j)
    if len(p) != len(q):
        return False
    newp = set()
    for x in range(len(p)):
        newp.add(p)
        p = p[1:] + p[0]
    return q in newp


def main(a, b):
    ans = 0
    for i in range(a, b + 1):
        for j in range(i+1, b + 1):
            if possible(i, j):
                ans += 1
    return ans


cases = int(input())

for case in range(cases):
    s = input().split()
    (a, b) = (int(s[0]), int(s[1]))
    ans = main(a, b)
    print('Case #{}: {}'.format(case + 1, ans))
