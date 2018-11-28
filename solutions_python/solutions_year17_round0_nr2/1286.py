#!/usr/bin/python3

import re

def solve(N):
    s = [c for c in str(N)]

    okay = False
    while not okay:
        for idx, num in enumerate(s):
            if idx == len(s) - 1:
                okay = True
                break

            if s[idx] <= s[idx + 1]:
                continue

            s[idx] = chr(ord(s[idx]) - 1)
            for jdx in range(idx + 1, len(s)):
                s[jdx] = '9'

            break


    return int(''.join(s))


def main():
    T = int(input())

    for idx in range(T):
        N = int(input())

        result = solve(N)

        print('Case #{}: {}'.format(idx + 1, result))

if __name__ == '__main__':
    main()
