# coding: utf-8


def flip(s, K, i):
    # i: 0 ~ len(s) - K
    for j in range(i, i + K):
        s[j] = not s[j]
    return s


def solve():
    S, K = input().strip().split()
    s = [c == "+" for c in S]
    K = int(K)
    l = len(s)

    cnt = 0
    for i in range(0, l - K + 1):
        if not s[i]:
            s = flip(s, K, i)
            cnt += 1
    if False not in s[l - K:]:
        return str(cnt)
    return "IMPOSSIBLE"


def main():
    n_cases = int(input())
    for i in range(n_cases):
        print("Case #{}: {}".format(i + 1, solve()))


main()
