#!/usr/bin/python3

def solve2(A):
    n = len(A)
    count = [0] * 2
    for i in range(n):
        count[A[i] % 2] += 1
    return count[0] + (count[1] + 1) // 2


def solve3(A):
    n = len(A)
    count = [0] * 3
    for i in range(n):
        count[A[i] % 3] += 1
    left = max(count[1], count[2]) - min(count[1], count[2])
    return count[0] + min(count[1], count[2]) + (left + 2) // 3

def solve4(A):
    n = len(A)
    count = [0] * 4
    for i in range(n):
        count[A[i] % 4] += 1
    ans = count[0] + (count[2] + 1) // 2
    count[2] %= 2
    t = min(count[1], count[3])
    ans += t
    count[1] -= t
    count[3] -= t
    if count[2] == 1 and max(count[1], count[3]) >= 2:
        ans += 1 + (max(count[1] - 2, count[3] - 2) + 3) // 4
    else:
        ans += (max(count[1], count[3]) + 3) // 4
    return ans

def solve():
    n, p = map(int, input().split())
    A = list(map(int, input().split()))
    if p == 2:
        return solve2(A)
    elif p == 3:
        return solve3(A)
    return solve4(A)

t = int(input())
for i in range(t):
    print("Case #{}: {}".format(i + 1, solve()))
