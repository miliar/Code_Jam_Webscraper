import os
import sys

def maxTriple(a, b, c):
    if a > b:
        return a if a > c else c
    else:
        return b if b > c else c

def task1(T1, T2, T3, c1, c2, c3):
    if T1 < T2:
        T1, T2 = T2, T1
        c1, c2 = c2, c1
    if T1 < T3:
        T1, T3 = T3, T1
        c1, c3 = c3, c1
    if T1 > T2 + T3:
        return False, ""
    ans = ""
    g = T2 + T3 - T1
    for _ in range(T2 + T3 - T1):
        ans += c1 + c2 + c3
    for _ in range(T2 - g):
        ans += c1 + c2
    for _ in range(T3 - g):
        ans += c1 + c3
    return True, ans


if __name__ == "__main__":
    with open('B-small-attempt0.in', 'r') as f:
        T = int(f.readline())
        for i in range(T):
            _, T1, T12, T2, T23, T3, T13 = [int(k) for k in f.readline().strip().split(' ')]
            ok, ans = task1(T1, T2, T3, 'R', 'Y', 'B')
            if ok:
                print("Case #%d: %s" % (i+1, ans))
            else:
                print("Case #%d: %s" % (i+1, "IMPOSSIBLE"))
