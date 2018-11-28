#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys


def pancake(s, k):
    count = 0
    for i in range(len(s) - k + 1):
        if s[i] == "-":
            count += 1
            s = swap(s, i, k)

    if '-' in s:
        return "IMPOSSIBLE"
    else:
        return count


def swap(s, i, k):
    # print("swap", str(i), str(k))
    slist = list(s)
    # print(s)
    for j in range(k):
        if slist[i+j] == '-':
            slist[i+j] = '+'
        elif slist[i+j] == '+':
            slist[i+j] = '-'
    # print("".join(slist))
    return "".join(slist)


with sys.stdin as f:
    T = int(f.readline())
    for i in range(T):
        line = f.readline().split()
        s, k = line[0], int(line[1])
        result = pancake(s, k)
        print("Case #" + str(i+1) + ": " + str(result))
