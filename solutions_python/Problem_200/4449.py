#!/usr/bin/env pypy3


def isTidy(n):
    s = str(n)
    m = '0'
    for i, c in enumerate(s):
        if c < m:
            return False
        m = c
    return True


def isListTidy(l):
    m = '0'
    for c in l:
        if c < m:
            return False
        m = c
    return True


def reverse_enum(L):
    for index in reversed(range(len(L))):
        yield index, L[index]


def dec(l):
    for i, c in reverse_enum(l):
        if c == '0':
            l[i] = '9'
        else:
            l[i] = chr(ord(c) - 1)
            return


def is_pow_10(l):
    if l[0] != '1':
        return False
    for c in l[1:]:
        if c != '0':
            return False
    return True


def find_tidy(l):
    p = l[0]
    I = 0
    found = False
    for i, c in enumerate(l):
        if c < p:
            l[i-1] = chr(ord(l[i-1])-1)
            l[i] = '9'
            I = i
            found = True
            break
        p = l[i]
    if found:
        for i in range(I, len(l)):
            l[i] = '9'


T = int(input())
tidy = []
for i in range(0, T):
    t = int(input())
    if t == 0:
        tidy.append(0)
    ls = list(str(t))
    while not isListTidy(ls):
        if is_pow_10(ls):
            ls = list(str(t-1))
        else:
            find_tidy(ls)
    tidy.append(int("".join(ls)))

"""
for i in range(0, T):
    t = int(input())
    if t == 0:
        tidy.append(0)
    ls = list(str(t))
    for n in range(t, 0, -1):
        if isListTidy(ls):
            tidy.append(n)
            break
        dec(ls)
"""
"""
for i in range(0, T):
    t = int(input())
    for n in range(t, 0, -1):
        if isTidy(n):
            tidy.append(n)
            break
"""


for i, n in enumerate(tidy):
    print("Case #{}: {}".format(i+1, n))
