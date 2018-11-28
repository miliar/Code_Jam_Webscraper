#!/usr/bin/env python3.5

n = int(input())
for t in range(1, n + 1):
    print('Case #{}: '.format(t), end='')
    c = input()
    i, w = c.split(' ')
    w = int(w)
    i = [1 if c == '-' else 0 for c in i]
    a = 0
    impo = False
    while sum(i) > 0:
        here = i.index(1)
        here = min(len(i) - w, here)
        for wow in range(here, here + w):
            i[wow] = (i[wow] + 1) % 2
        a += 1
        if a > 100000:
            impo = True
            break
    if impo:
        print('IMPOSSIBLE')
    else:
        print(a)
