T = int(input())

import math
pi = math.pi
def compute(Ra, Ha):
    return Ra*Ra*pi+2*pi*Ra*Ha
    pass


for t in range(T):
    N, K = map(int, input().split())
    temp = [[(0, 0) for _ in range(K)] for _ in range(N)]
    pancakes = []
    for _ in range(N):
        pancakes.append(tuple(map(int, input().split())))
    pancakes.sort(reverse = True)
    for k in range(K):
        temp[0][k] = (0, 0)
    for n in range(N):
        m = 0
        for i in range(n+1):
            R, H = pancakes[i]
            m = max(m, compute(R, H))
        temp[n][0] = (m, 0)
    for n in range(1, N):
        for k in range(1, K):
            r_1, h_1 = pancakes[temp[n-1][k-1][1]]
            r, h = pancakes[n]
            a = temp[n-1][k-1][0] + 2*r*h*pi
            temp[n][k] = temp[n-1][k]
            if a > temp[n][k][0]:
                temp[n][k] = (a, n)
    s = 0
    print("Case #{}:".format(t+1), temp[-1][-1][0])
