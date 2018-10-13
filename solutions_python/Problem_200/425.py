#!/usr/bin/env python

from sys import stdin, stdout

cases = int(stdin.readline())


def last_tidy(line):
    n = map(int, line.rstrip())
    l = len(n)
    for i in range(l-2, -1, -1):
        if n[i] > n[i+1]:
            n[i] -= 1
            for j in range(i+1, l):
                n[j] = 9
    return int(''.join([str(_) for _ in n]))


for case in range(cases):
    stdout.write("Case #%d: %d\n" % (case+1, last_tidy(stdin.readline())))
