#!/usr/bin/env python3


import sys

def flip(pan, k):
    if not '-' in pan:
        return 0
    pos = pan.index('-')
    if len(pan[pos:]) < k:
        return "IMPOSSIBLE"
    for i in range(pos, pos+k):
        pan[i] = '+' if pan[i] == '-' else '-'

    f = flip(pan[pos:], k)
    try:
        return 1 + f
    except TypeError:
        return f


def main():
    sys.setrecursionlimit(150000)
    t = int(input())
    for i in range(1, t+1):
        pan, k = input().split()
        k = int(k)
        pan = list(pan)
        print("Case #{}: ".format(i), end='')
        print(flip(pan, k))


if __name__ == '__main__':
    main()
