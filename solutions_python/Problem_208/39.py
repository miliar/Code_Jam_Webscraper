import os
import sys


def Min(a, b):
    if a < 0:
        return b
    if b < 0:
        return a
    return min(a, b)


if __name__ == "__main__":
    with open('C-large.in', 'r') as f:
        T = int(f.readline())
        for tt in range(T):
            n, Q = [int(k) for k in f.readline().strip().split(' ')]
            # print(n, q)
            s = [0.0] * n
            e = [0.0] * n
            mp = []
            for j in range(n):
                e[j], s[j] = [float(k) for k in f.readline().strip().split(' ')]
                mp.append([])
            for j in range(n):
                mp[j] = [float(k) for k in f.readline().strip().split(' ')]
            
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        if mp[i][k] >= 0 and mp[k][j] >= 0:
                            mp[i][j] = Min(mp[i][j], mp[i][k] + mp[k][j])

            ans = []
            for q in range(Q):
                st, ed = [int(k) for k in f.readline().strip().split(' ')]
                dp = [-1.0] * n
                dp[st - 1] = 0.0
                mark = [False] * n
                while True:
                    k = -1
                    for j in range(n):
                        if not mark[j] and dp[j] >= 0 and (k < 0 or dp[j] < dp[k]):
                            k = j
                    if k < 0:
                        break
                    mark[k] = True
                    for j in range(n):
                        if not mark[j] and mp[k][j] >= 0 and mp[k][j] <= e[k]:
                            dp[j] = Min(dp[j], dp[k] + mp[k][j] / s[k])
                ans.append(dp[ed - 1])
            print("Case #%d: %s" % (tt+1, ' '.join([str(a) for a in ans])))
