def getP(n):
    p = 0
    ex = 1
    while ex <= n:
        ex *= 2
        p += 1
    return p-1

def getMinMax(N, p):
    m = (N-1)/2
    M = m + (1 if N%2 == 0 else 0)
    # print m, M
    if p-1 == 0:
        return m, M
    childm = getMinMax(m,p-1)
    childM = getMinMax(M,p-1)
    return min(min(childm), min(childM)), max(max(childm), max(childM))


def solv(N, K):
    if K == 1:
        return getMinMax(N, 1)
    p = getP(K)
    m, M = getMinMax(N, p)
    if N - (m * 2 ** p + K - 1) > 0:
        return getMinMax(M, 1)
    return getMinMax(m, 1)

def main():
    n = int(raw_input())
    for i in range(n):
        N, K = map(int, raw_input().split(' '))
        m, M = solv(N, K)
        print "Case #%d: %d %d" %(i+1, M, m)

if __name__ == "__main__":
    main()