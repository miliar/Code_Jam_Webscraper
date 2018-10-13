# coding=utf-8
# Author: Jianghan LI
# Question: A. Oversized Pancake Flipper
# Date: 2017-04-08 14:37


def solve(S, K):
    S = [c == '+' for c in S]
    i = len(S) - 1
    res = 0
    while i >= 0:
        if S[i] == 0:
            if i < K - 1:
                return "IMPOSSIBLE"
            for j in range(K):
                S[i - j] ^= 1
            res += 1
        i -= 1
    return res

T = int(raw_input())  # read a line with a single integer
for i in xrange(T):
    S, K = raw_input().split(" ")
    res = solve(S, int(K))
    print "Case #{}: {}".format(i + 1, res)
