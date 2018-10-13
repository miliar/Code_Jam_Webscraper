# -*- coding: utf-8 -*-
from sys import stdin, stdout


stdin = open('A-large.in', 'r')
stdout = open('A-large.out', 'w')


def solve():
    l = stdin.readline().rstrip().split()
    n, s = int(l[0]), l[1].rstrip()
    cnt, tmp = 0, 0
    for i in range(n+1):
        a = int(s[i])
        if tmp < i:
            cnt += i - tmp
            tmp = i
        tmp += a
    stdout.write('%d\n' % cnt)

T = int(stdin.readline())
for t in range(T):
    stdout.write('Case #%d: ' % (t+1))
    solve()