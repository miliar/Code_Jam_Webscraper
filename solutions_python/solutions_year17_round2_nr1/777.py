#!/usr/bin/python3


def solve(*args):
    return None

T = int(input())
for Ti in range(T):
    D, N = map(int, input().strip().split(" "))
    last = 0
    for Ni in range(N):
        Ki, Si = map(int, input().strip().split(" "))
        time = float(D - Ki) / Si
        if time > last:
            last = time
    ans = D / last
    print("Case #{}: {}".format(Ti+1, ans))
