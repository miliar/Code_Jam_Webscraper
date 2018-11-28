#problem A

import itertools

def solvecase(G,I,J):
    try:
        for i in range(I):
            for j in range(J):
                if G[i][j]=='#':
                    if G[i+1][j]==G[i][j+1]==G[i+1][j+1]=='#':
                        G[i][j] = G[i+1][j+1] = '/'
                        G[i][j+1] = G[i+1][j] = '\\'
                    else:
                        return None
    except:
        return None
    return G

def printmat(G,I):
    for i in range(I):
        print(''.join(G[i]))

N = int(input())

for n in range(N):
    I,J = map(int,input().split(' '))
    G = []
    for i in range(I):
        G.append(list(itertools.chain(input())))
    R = solvecase(G,I,J)
    print('Case #'+str(n+1)+':')
    if R:
        printmat(R,I)
    else:
        print("Impossible")
