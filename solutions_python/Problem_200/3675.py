#!/usr/bin/env python3

import os
import sys

def is_tidy(n):
    perv_i = int(str(n)[-1])
    for i in list(reversed(str(n)[:-1])):
        if perv_i < int(i):
            return False
        else:
            perv_i = int(i)

    return True

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        last_tidy = 0
        for j in range(N, 0, -1):
            if is_tidy(j):
                last_tidy = j
                break

        print('Case #{}: {}'.format(i + 1, last_tidy))


if __name__ == '__main__':
    main()
