import itertools
import operator
fname = "C-small-1-attempt0"

def boost(Y,U,K):
    X1 = Y[:-K]
    X2 = Y[-K:]
    while U > 10**-7:
        n = 1
        while n < len(X2) and X2[n] - X2[0] < 10**-7:
            n += 1
        u = U / n if n == len(X2) else min(U / n, X2[n] - X2[0])
        for i in range(n):
            X2[i] += u
            U -= u
    return X1 + X2

def P(X, K, pGrid):
    N = len(X)
    if K == 0:
        return 1.0
    if pGrid[N-1][K-1] < -10**-7:
        if K > N:
            pGrid[N-1][K-1] = 0.0
        elif N == K and N == 1:
            pGrid[0][0] = X[0]
        else:
            pGrid[N-1][K-1] = X[-1] * P(X[:-1],K-1,pGrid) \
                    + (1 - X[-1]) * P(X[:-1],K,pGrid)
    return pGrid[N-1][K-1]




    p = 0.0
    s = K
    while s <= N:
        succs = [x for x in itertools.combinations(range(N),s)]
        for I in succs:
            p+=reduce(operator.mul, [X[i] if i in I else (1-X[i]) for i in range(N)], 1)
    return p

with open(fname + ".in","r") as f:
    inp = [l.strip('\n') for l in f.readlines()]

f = open(fname + ".out","w")
for i in range(int(inp[0])):
    t = inp[3*i+1].split(' ')
    N = int(t[0])
    K = int(t[1])
    U = float(inp[3*i+2])
    Y = [float(x) for x in inp[3*i+3].split(' ')]
    Y.sort()
    X = boost(Y,U,K)
    pGrid = [[-1.0 for k in range(K)] for j in range(N)]
    prob = P(X, K, pGrid)
    f.write("Case #" + str(i+1) + ": " + str(prob) + "\n")

f.close()
