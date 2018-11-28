#!/usr/bin/python


def ispal(n):
    s = str(n)
    return s == s[::-1]


def c(A, B):
    count = 0
    for x in range(A, B + 1):
        sqx = int(x**0.5)
        if sqx**2 != x:
            continue
        if ispal(x) and ispal(sqx):
            count += 1
    return count


T = int(input())
for tc in range(T):
    inp = input().strip().split()
    A, B = int(inp[0]), int(inp[1])
    print('Case #{}: {}'.format(tc + 1, c(A, B)))
