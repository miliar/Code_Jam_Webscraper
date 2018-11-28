import os
import sys


def flip(ch):
    if ch == '+':
        return '-'
    return '+'


def calc(st, k):
    s = [0 if ch == '-' else 1 for ch in st]
    cnt = 0
    for i in range(len(s) - k + 1):
        if s[i] == 0:
            cnt += 1
            for j in range(k):
                s[i + j] = 1 - s[i + j]
    for i in range(len(s)):
        if s[i] != 1:
            return 'IMPOSSIBLE'
    return str(cnt)


if __name__ == "__main__":
    with open('A-large.in', 'r') as f:
        n = int(f.readline())
        for i in range(n):
            st, k = f.readline().strip().split(' ')
            print("Case #%d: %s" % (i+1, calc(st, int(k))))
