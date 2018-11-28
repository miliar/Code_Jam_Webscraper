#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import ceil, floor
from random import randint
from collections import deque

def modulo(a, b, c):
    x = 1
    y = a

    while (b > 0):
        if (b & 1):
            x = (x * y) % c
        y = (y * y) % c
        b /= 2

    return x % c

def miller(p, iteration):
    if (p < 2):
        return False

    if (p < 4):
        return True

    if (p != 2 and p % 2 == 0):
        return False

    s = p - 1
    while (s % 2 == 0):
        s /= 2

    for i in range(iteration):
        a = randint(1, p - 1)
        temp = s

        mod = modulo(a, temp, p)
        while (temp != p - 1 and mod != 1 and mod != p - 1):
            mod = (mod * mod) % p
            temp *= 2

        if (mod != p - 1 and temp % 2 == 0):
            return False

    return True

def gcd(a, b):
    if (b == 0):
        return a

    return gcd(b, a % b)

def lcm(a, b):
    return a * b / gcd(a, b)

def f(x, n, c):
    return (x * x + c) % n

def pollard(n):
    x = 2
    y = 2
    d = 1
    c = randint(1, 10 ** 9)

    while (d == 1):
        x = f(x, n, c)
        y = f(f(y, n, c), n, c)
        d = gcd(abs(x - y), n)

    return d

def factorize(n):
    v = []
    q = deque()

    q.appendleft(n)
    while len(q):
        m = q.pop()

        if (miller(m, 10)):
            v.append(m)
            continue

        if (m % 2 == 0):
            q.appendleft(2)
            q.appendleft(m / 2)
            continue

        p = pollard(m)
        while(p == m):
            p = pollard(m)

        if (p != 1):
            q.appendleft(p)
            q.appendleft(m / p)

    v.sort()

    return v

def combs(v):
    i = 0
    w = []
    vv = []
    ans = []

    while(i < len(v)):
        j = i
        while(j < len(v) and v[i] == v[j]):
            j += 1

        vv.append(v[i])
        w.append(j - i)
        i = j

    ww = [0 for x in range(len(vv))]
    if (ww == []):
        return [1]

    while(True):
        temp = 1
        for i in range(len(ww)):
            temp *= vv[i] ** ww[i]

        ans.append(temp)

        i = len(ww) - 1
        aux = 1

        while(i >= 0):
            ww[i] += aux
            aux = 0

            if (ww[i] > w[i]):
                ww[i] = 0
                aux = 1

            i -= 1

        if (aux == 1):
            return ans

if __name__ == "__main__":
    t = int(raw_input())

    for tt in range(1, t + 1):
        v = []
        w = []
        n, l, h = [long(x) for x in raw_input().split()]

        v = [int(x) for x in raw_input().split()]
        found = -1

        for i in range(l, h + 1):
            j = 0
            while (j < len(v)):
                if (i % v[j] != 0 and v[j] % i != 0):
                    break
                j += 1

            if (j == len(v)):
                found = i
                break

        if (found == -1):
            print "Case #%d: NO" % tt
        else:
            print "Case #%d: %d" % (tt, found)
