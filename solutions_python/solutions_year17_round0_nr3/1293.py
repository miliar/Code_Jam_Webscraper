# coding=utf-8
# Author: Jianghan LI
# Question: Qualification Round 2017/C. Bathroom Stalls
# Date: 2017-04-08 16:50-17:33


def solve(N, K):
    from math import log
    exp = log(K + 1) // log(2)
    K1 = 2**exp - 1
    gap = (N - K1) // (K1 + 1)
    rest = (N - K1) % (K1 + 1)
    if K == K1:
        return "%d %d" % (gap + (rest > 0), gap)
    elif rest >= K - K1:
        return "%d %d" % ((gap + 1) // 2, gap // 2)
    else:
        return "%d %d" % (gap // 2, (gap - 1) // 2)

T = int(raw_input())
for i in xrange(T):
    N, K = map(int, raw_input().split())
    res = solve(N, K)
    print("Case #%d: %s" % (i + 1, res))
    # print "Case #", i + 1, N, K, res
