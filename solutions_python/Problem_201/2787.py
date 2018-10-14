def dist(N, S, i, d):
    o = -1
    while (i >= 0) and (i < N):
        if S[i]:
            break
        else:
            i += d
            o += 1
    return o

def left(S):
    L = []
    d = 0
    for s in S:
        if s:
            L.append(-1)
            d = 0
        else:
            L.append(d)
            d += 1
    return L

def right(S):
    return reversed(left(reversed(S)))

def think(N, K, S):
    while True:
        L = list(filter(lambda l: l >= 0, left(S)))
        R = list(filter(lambda r: r >= 0, right(S)))
        minLR = list(map(lambda it: min(it), zip(L, R)))
        maxminLR = max(minLR)
        imaxminLR = list(map(lambda v: v[0], filter(lambda p: p[1], enumerate(map(lambda s: s == maxminLR, minLR)))))
        if len(imaxminLR) == 1:
            chosen = imaxminLR[0]
        else:
            maxLR = list(map(lambda it: max(it), zip(L, R)))
            imaxminC = list(map(lambda i: [i, maxLR[i]], imaxminLR))
            maxC = max(imaxminC, key=lambda it: it[1])[1]
            chosen = min(map(lambda p: p[0], filter(lambda it: it[1] == maxC, imaxminC)))
        if K == 1:
            return max(L[chosen], R[chosen]), min(L[chosen], R[chosen])
        S[list(filter(lambda p: not p[1], enumerate(S)))[chosen][0]] = True
        K = K-1

def magic(N, K):
    if N <= K: return 0, 0
    S = [False] * N
    M, m = think(N, K, S)
    return M, m

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        line = input().split(' ')
        N, K = int(line[0]), int(line[1])
        M, m = magic(N, K)
        print('case #%d: %d %d' % (t+1, M, m))
