# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 08:59:48 2017

@author: DELL GAMING
"""

t = int(input())
for i in range(1, t + 1):
    list = [int(x) for x in input()]
    out = [0 for lol in range(len(list))]
    autotidy = 1
    if len(list) == 1:
        print('Case #{}: {}'.format(i, list[0]))
        continue
    for j in range(len(list)):
        if j == len(list) - 1:
            break
        if list[j] <= list[j+1]:
            out[j], out[j+1] = list[j], list[j+1]
        else:
            autotidy = 0
            break
    k = len(list) - 1
    if autotidy == 0:
        if list[j] == 1:
            print('Case #{}: {}'.format(i, '9'*(len(list) - 1)))
            continue
        else:
            store = list[j]
            k = list.index(store)
            out[k] = store - 1
    print('Case #{}: '.format(i), end = '')
    for d in range(0, k + 1):
        print(out[d], end = '')
    print('9'*(len(list)-1-k))