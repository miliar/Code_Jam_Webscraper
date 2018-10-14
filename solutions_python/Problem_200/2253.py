#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def is_increasing(num):
    s = str(num)
    isit = True
    for i in range(len(s) - 1):
        if int(s[i]) > int(s[i + 1]):
            isit = False
            break
    return isit


def decrease(num):
    # print(num)
    s = str(num)
    pos = -1
    for i in range(len(s) - 1):
        if int(s[i]) > int(s[i + 1]):
            pos = i

    # change all for nines
    v = str(int(s[pos]) - 1)
    val = s[:pos] + v + '9' * (len(s) - pos - 1)
    val = int(val)
    # print(val)
    return val

# compute tidy numbers up to limit
limit = 1001
tidy = list()
num = 1
while num < limit:
    if is_increasing(num):
        tidy.append(num)
    num += 1

T = int(input())  # number of test cases
for t in range(T):
    N = int(input())  # nth tidy number
    res = N
    while not is_increasing(res):
        res = decrease(res)  # large dataset
        # res -= 1  # small dataset
    print("Case #{:d}: {}".format(t + 1, res))
