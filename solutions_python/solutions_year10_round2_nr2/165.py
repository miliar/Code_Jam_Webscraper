import sys

def getnum():
    return [int(x) for x in sys.stdin.readline().split()]


def sortcount(A, L, k):
    s = 0
    t = 0
    for a in range(len(A)):
        i = A[a]
        if i <= L:
            s += a-t
            k -= 1
            t += 1
        if k == 0:
            return s
    return -1

C, = getnum()

for c in range(1, C+1):
    N, K, B, T = getnum()

    X = list(reversed(getnum()))
    V = list(reversed(getnum()))

    D = [B - x for x in X]
    M = [float(D[i])/V[i] for i in range(N)]

    if K == 0:
        sol = 0
    else:
        for n in range(N):
            if K == 0:
                sol = 0
                break
            i = M[n]
            if i <= T:
                K -= 1
            else:
                sol = sortcount(M[n:], T, K)
                if sol == -1:
                    sol = "IMPOSSIBLE"
                break
            if K == 0:
                sol = 0
                break

    print "Case #%d:" % (c), sol
