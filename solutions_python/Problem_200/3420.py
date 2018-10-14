#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 09:38:41 2017

@author: txmy
"""

n = int(input())
for i in range(n):
    sl = input()
    sl2 = list(sl)
    ret = []
    for j in range(len(sl2)):
        k = len(sl2) - j - 1
        if k > 0:
            if int(sl2[k]) < int(sl2[k - 1]):
                for m in range(len(ret)):
                    ret[m] = '9'
                ret.append('9')
                sl2[k - 1] = str(int(sl2[k - 1]) - 1)
            else:
                ret.append(sl2[k])
        else:
            if int(sl2[0]) > 0:
                ret.append(sl2[0])

    flg = False
    out = ''
    ret.reverse()
    for s in ret:
        out += s
    print(('Case #{0}: '+out).format(i+1))
