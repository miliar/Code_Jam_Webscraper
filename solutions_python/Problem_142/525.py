
def sol(N, L):
    X = [0] * N
    FALSE = 'Fegla Won'
    c = 0
    while True:
        D = [0] * N
        fin = True
        for i in xrange(1, N):
            while X[i] < len(L[i]) and L[i][X[i]] == L[0][X[0]]:
                D[i] += 1
                X[i] += 1
            if X[i] < len(L[i]):
                fin = False
            if D[i] == 0:
                return FALSE
        px = X[0]
        while X[0] < len(L[0]) and L[0][X[0]] == L[0][px]:
            D[0] += 1
            X[0] += 1
        sm0 = sum(D)
        sm = sm0/N
        if sm0 % N != 0 and (0.5 * N < (sm0 % N)):
            sm += 1
        # print D, sm
        for d in D:
            c += abs(sm - d)
        # print X[0], L[0]
        if X[0] >= len(L[0]):
            if fin is False:
                return FALSE
            break
    
    return c
    

import sys
readline = sys.stdin.readline

line = readline()
tn = int(line)
for i in xrange(1, tn + 1):
    N = int(readline())
    lines = [readline().strip() for q in xrange(N)]
    print 'Case #{}: {}'.format(i, sol(N, lines))

