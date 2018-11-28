#!/usr/bin/env python3


def answer(n, k):
    if n % 2 == 1:
        h, l = n // 2, n // 2
    else:
        h, l = n // 2, n // 2 - 1
    if k == 1:
        return h, l
    if k % 2 == 0:
        return answer(h, k // 2)
    else:
        return answer(l, k // 2)


T = int(input())
for count in range(T):
    N, K = (int(x) for x in input().split())
    a, b = answer(N, K)
    print("Case #", count + 1, ": ", a, ' ', b, sep='')
