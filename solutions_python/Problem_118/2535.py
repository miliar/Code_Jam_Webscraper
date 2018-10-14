#!/usr/bin/env python
# -*- coding: utf-8 -*


def solve(a, b):
    out = 0

    maxi = int(b**0.5)
    for k in range(maxi + 1):
        sk = str(k)
        if sk == sk[::-1]:
            k2 = k**2
            sk2 = str(k2)
            if sk2 == sk2[::-1]:
                if k2 in range(a, b+1):
                    out += 1

    return out


if __name__ == "__main__":
    T = int(input())  # nb of test cases

    for x in range(T):
        A, B = map(int, input().split())

        y = solve(A, B)
        print("Case #%d: %s" % (x+1, y))
