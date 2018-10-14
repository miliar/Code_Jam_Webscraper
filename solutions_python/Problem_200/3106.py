#!/usr/bin/env python
# -*- coding: utf-8 -*

"""GCJ 2017 Qualification Round: Problem B"""


def solve(n):
    n_list = list(str(n))
    n_len = len(n_list)
    n_inv = n_list[::-1]

    for i in range(n_len - 1):
        if int(n_inv[i]) < int(n_inv[i+1]) or n_inv[i] == '0':
            for j in range(i):
                n_inv[j] = '9'
            n_inv[i] = '9'
            n_inv[i+1] = str(int(n_inv[i+1]) - 1)

            if n_inv[i+1] == '-1':
                n_inv[i+1] = '0'


    return int(''.join(n_inv[::-1]))



if __name__ == "__main__":
    T = int(input())  # nb of test cases

    for x in range(T):
        N = int(input().strip())

        y = solve(N)
        print("Case #%d: %d" % (x+1, y))
