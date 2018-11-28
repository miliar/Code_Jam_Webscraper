#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

vowels = ['a', 'e', 'i', 'o', 'u']

def ans(s, n):
    def countif(s):
        for i in range(len(s)-n+1):
            a = True
            for ss in s[i:i+n]:
                a = a and ss not in vowels
            if a:
                return True
        return False

    l = len(s)
    c = 0
    for j in range(n, l+1):
        for i in range(0, l - n + 1):
            if i+j<=l and countif(s[i:i+j]):
                c += 1
    return c


with open(sys.argv[1]) as fr, open('a.out', 'w') as fw:
    T = int(fr.readline())
    for i in range(T):
        no = i + 1
        s, n = fr.readline().split()
        n = int(n)
        fw.write("Case #{no}: {ans}\n".format(no=no,ans=ans(s, n)))


# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
