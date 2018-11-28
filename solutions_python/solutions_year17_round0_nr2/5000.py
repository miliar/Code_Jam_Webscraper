# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 08:51:50 2017

@author: Lonardi
"""


def is_tidy(N):
    tidy = True
    digits = [int(d) for d in str(N)]
    # print(digits)
    for z in range(len(digits) - 1):
        tidy = (digits[z] <= digits[z + 1])
        # print(tidy, digits[z], digits[z + 1])
        if not tidy:
            break
    return(tidy)

t = int(input())

for i in range(1, t + 1):
    n = int(input())
    for j in range(n, 0, -1):
        if(is_tidy(j)):
            break
    print("Case #{}: {}".format(i, j))
