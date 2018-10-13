# -*- coding: utf-8 -*-
from sys import stdin, stdout


filename = 'C-small-attempt0'
stdin = open(filename + '.in', 'r')
stdout = open(filename + '.out', 'w')


def solve():
    X, L = [int(item) for item in stdin.readline().split()]
    s = stdin.readline().rstrip() * L
    dp = [s[0]]
    for i in range(1, len(s)):
        dp.append(opt(dp[i-1], s[i]))
    if judge(dp):
        stdout.write('YES\n')
    else:
        stdout.write('NO\n')


def opt(x, y):
    bcnt = 0
    if x.startswith('-'):
        bcnt += 1
        x = x[1:]
    if y.startswith('-'):
        bcnt += 1
        y = y[1:]
    ret = 0
    if x == '1' or y == '1':
        ret = y
    elif x == y:
        ret = '1'
        bcnt += 1
    elif x == 'i':
        if y == 'j':
            ret = 'k'
        else:
            ret = 'j'
            bcnt += 1
    elif x =='j':
        if y == 'i':
            ret = 'k'
            bcnt += 1
        else:
            ret = 'i'
    else:
        if y == 'i':
            ret = 'j'
        else:
            ret = 'i'
            bcnt += 1
    if bcnt % 2 == 1:
        ret = '-' + ret
    return ret

def judge(dp):
    if dp[-1] != '-1':
        return False
    for i in range(len(dp)-1):
        if dp[i] == 'i':
            for j in range(i+1, len(dp)):
                if dp[j] == 'k':
                    return True

T = int(stdin.readline())
for t in range(T):
    stdout.write('Case #%d: ' % (t+1))
    solve()