# coding=utf-8
# Author: Jianghan LI
# Question: Qualification Round 2017/B. Tidy Numbers
# Date: 2017-04-08 14:54-15:38


def solve(N):
    for i in range(1, len(N)):
        if N[i - 1] > N[i]:
            if N[i - 1] == '1':
                return '9' * (len(N) - 1)
            j = i
            while j > 0 and N[j - 1] == N[i - 1]:
                j -= 1
            return N[:j] + str(int(N[j]) - 1) + '9' * (len(N) - 1 - j)
    return N

T = int(raw_input())
for i in xrange(T):
    N = raw_input()
    res = solve(N)
    # print("Case #%d: %s %s" % (i + 1, N, res))
    print("Case #%d: %s" % (i + 1, res))

##### Test Case #####
# print solve('111222333299')
# print solve('2222099')
# print solve('2099')
# print solve('11110134')
