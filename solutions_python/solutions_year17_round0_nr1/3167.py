import numpy as np

def flip(C,S,K):
    X = []
    for s in S:
        if s == '+':
            X.append(1)
        else:
            X.append(0)
    FLIP = 0
    for i in range(len(X)-K+1):
        if X[i] == 0:
            FLIP += 1
            for j in range(K):
                X[i+j] = 1-X[i+j]
    if np.all(X):
        return 'Case #'+str(C)+': '+str(FLIP)+'\n'
    else:
        return 'Case #'+str(C)+': IMPOSSIBLE\n'
        
W = open('Crepe.res2','w')
F = open('Crepe.in2','r')
F.readline()
C = 0
for L in F:
    S,K = L[:-1].split(' ')
    K = int(K)
    C += 1
    W.write( flip(C,S,K) )

W.close()
F.close()
