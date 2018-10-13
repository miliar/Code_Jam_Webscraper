#!/usr/bin python

import sys

input = sys.stdin


def data():
    input.readline()
    for l in input:
        yield l.strip()


def results(f=None):
    for i, l in enumerate(data()):
        print "Case #" + str(i + 1) + ":", f(l)


def calc(l=None):
    A, B = map(int, l.split(' '))
    r = 0
    for n in range(A, B):
        s = str(n)
        lenght = len(s)
        k = {}
        for i in range(1, lenght):
            m = s[i:] + s[:i]
            m = int(m)
            if A <= n < m <= B:
                k[m] = 1
        r += len(k)
    return r

if __name__ == "__main__":
    f = calc
    results(f)
