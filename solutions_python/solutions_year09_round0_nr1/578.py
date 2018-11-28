#!/usr/bin/python
import sys, os

(L, D, N) = sys.stdin.readline().split()
L = int(L)
D = int(D)
N = int(N)

def read_word(s):
    w = []
    for i in s:
        w.append(1 << (ord(i) - ord('a')))
    return w

def read_test(s):
    w = []
    in_g = False
    for i in s:
        if i == '(':
            in_g = True
            g = 0
        elif i == ')':
            in_g = False
            w.append(g)
        elif in_g:
            g += 1 << (ord(i) - ord('a'))
        else:
            w.append(1 << (ord(i) - ord('a')))
    return w

def match(t, s):
    for i in range(L):
        if t[i] & s[i] != s[i]:
            return False
    return True

a = []

for i in range(D):
    ws = sys.stdin.readline().strip()
    w = read_word(ws)
    a.append(w)

for j in range(N):
    ts = sys.stdin.readline().strip()
    t = read_test(ts)

    count = 0
    for i in range(D):
        if match(t, a[i]):
            count += 1
    sys.stdout.write("Case #%d: %d\n" % (j + 1, count))

