#!/usr/bin/python3

def solve(mis):
    biggest = 0

    ret1= 0
    for i, mi in enumerate(mis):
        try:
            diff = mi - mis[i+1]
            if diff > 0:
                ret1 += diff
                if diff > biggest:
                    biggest = diff
        except IndexError:
            break

    ret2 = 0
    for i, mi in enumerate(mis):
        try:
            mis[i+1]
            ret2 += min(biggest, mi)
        except IndexError:
            break
    return ret1, ret2

T = int(input())
for t in range(T):
    _ = input()
    mis = list(map(int, input().strip().split()))
    a1, a2 = solve(mis)
    print("Case #%d: %d %d" % (t+1, a1, a2))
