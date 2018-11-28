#!/usr/bin/env python3.5

def tidy(c):
    s = str(c)
    b = 0
    for t in s:
        if int(t) < b:
            return False
        b = int(t)
    return True

n = int(input())
for t in range(1, n + 1):
    print('Case #{}: '.format(t), end='')
    c = int(input())
    while not tidy(c):
        c -= 1
    print(c)
