# -*- coding: utf-8 -*-


def flip(S, K, i):
    for j in range(K):
        if S[i + j] == '+':
            S[i + j] = '-'
        else:
            S[i + j] = '+'


def happy(S):
    return not ('-' in S)

def f(S, K):
    cnt = 0
    for i in range(len(S) - K + 1):
        if S[i] == '-':
            flip(S, K, i)
            cnt += 1

    if happy(S):
        return cnt
    else:
        return -1


def main():
    T = int(input())
    for i in range(T):
        x = i + 1

        S, K = input().split()
        S = list(S)
        K = int(K)
        ans = f(S, K)
        if ans == -1:
            y = "IMPOSSIBLE"
        else:
            y = str(ans)

        print("Case #%d: %s" % (x, y))


if __name__ == '__main__':
    main()
