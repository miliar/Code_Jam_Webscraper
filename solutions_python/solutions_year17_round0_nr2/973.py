#!/usr/bin/env python3
pr = lambda n, m: print("Case #{}: {}".format(n,m))
def istidy(num):
    s = [c for c in str(num)]
    s.sort()
    return num == int(''.join(s))

n = int(input())
for i in range(n):
    c = int(input())
    if istidy(c):
        pr(i+1, c)
        continue
    last = lambda p: (c//(10**(p-1)))%(10)
    ctr = 1
    while not istidy(c):
        a = last(ctr)
        c -= ((10 ** (ctr - 1)) * (a+1))
        ctr += 1
    pr(i+1, c)
