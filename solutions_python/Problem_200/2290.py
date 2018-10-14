#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def istidy(n):
    a = str(n)
    tmp = a[0]
    for char in a[1:]:
        if char < tmp:
            return False
        tmp = char
    return True


def lasttidy(n):
    while True:
        if istidy(n):
            return n
        n = n - 1


nt = int(input())
for i in range(nt):
    target = input()
    print("Case #{0}: {1}".format(i+1, lasttidy(int(target))))


