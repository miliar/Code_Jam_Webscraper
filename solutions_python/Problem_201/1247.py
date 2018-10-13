from sys import *

def readints():
    return list(map(int, stdin.readline().split()))

def evaluateFast(N):
    if N % 2 == 0:
        k = N // 2 - 1
    else:
        k = N // 2
    return k, min(k, N - k - 1), max(k, N - k - 1)

def insert(N, K):
    if N == 0:
        return (-np.inf, -np.inf)
    if N == 1:
        return (0, 0)

    k, m, M = evaluateFast(N)

    if K == 1:
        return (m, M)

    K -= 1

    nk = K - K // 2 if k >= N - k - 1 else K // 2

    if K % 2 == 0:
        if k >= N - k - 1:
            return insert(N - k - 1, K - nk)
        else:
            return insert(k, nk)
    else:
        if k >= N - k - 1:
            return insert(k, nk)
        else:
            return insert(N - k - 1, K - nk)


T, = readints()

for i in range(T):
    N, K = readints()

    m, M = insert(N, K)

    print("Case #{}: {} {}".format(i + 1, int(M), int(m)))
    # exit()
