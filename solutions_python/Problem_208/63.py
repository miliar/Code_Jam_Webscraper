import argparse
import math
import sys
parser = argparse.ArgumentParser(description='Google Code Jam 2017')
parser.add_argument('fin')
parser.add_argument('fout')

args = parser.parse_args()

fin = args.fin
fout = args.fout


def argmin(l, q):
    argmin = next(iter(q))
    min = l[argmin]
    for i in range(len(l)):
        if i in q and l[i] < min:
            min = l[i]
            argmin = i
    return argmin


def solver(N, Q, E, S, D, U, V):
    DD = []
    PP = []

    for n in range(N):
        q = set(range(N))
        dist = []
        prev = []

        # init
        for i in range(N):
            dist.append(sys.float_info.max)
            prev.append(-1)

        dist[n] = 0

        while len(q) > 0:
            u = argmin(dist, q)
            q.remove(u)

            for v in range(N):
                if D[u][v] != -1: # has route
                    alt = dist[u] + D[u][v]
                    if alt < dist[v]:
                        dist[v] = alt
                        prev[v] = u
        DD.append(dist)
        PP.append(prev)

    for i in range(N):
        for j in range(N):
            if DD[i][j] > E[i]:
                DD[i][j] = sys.float_info.max
            else:
                DD[i][j] = DD[i][j] / S[i]

    #DD[i][j]: min time needed from i to j


    DDD = []
    PPP = []

    for n in range(N):
        q = set(range(N))
        dist = []
        prev = []

        # init
        for i in range(N):
            dist.append(sys.float_info.max)
            prev.append(-1)

        dist[n] = 0

        while len(q) > 0:
            u = argmin(dist, q)
            q.remove(u)

            for v in range(N):
                if DD[u][v] != -1: # has route
                    alt = dist[u] + DD[u][v]
                    if alt < dist[v]:
                        dist[v] = alt
                        prev[v] = u
        DDD.append(dist)
        PPP.append(prev)

    ret = []
    for i in range(len(U)):
        ret.append(str(DDD[U[i]-1][V[i]-1]))

    return " ".join(ret)


with open(fin, 'r') as input, open(fout, 'w') as output:
    T = int(input.readline().rstrip('\n'))
    for i in range(0, T):
        tkn = input.readline().rstrip('\n').split(' ')
        N = int(tkn[0])
        Q = int(tkn[1])
        E = []
        S = []
        D = []
        U = []
        V = []
        for j in range(N):
            tkn = input.readline().rstrip('\n').split(' ')
            E.append(int(tkn[0]))
            S.append(int(tkn[1]))
        for j in range(N):
            tkn = input.readline().rstrip('\n').split(' ')
            Di = [int(d) for d in tkn]
            D.append(Di)
        for j in range(Q):
            tkn = input.readline().rstrip('\n').split(' ')
            U.append(int(tkn[0]))
            V.append(int(tkn[1]))
        answer = 'Case #{}: {}\n'.format(i + 1, solver(N, Q, E, S, D, U, V))
        print(answer)
        output.write(answer)
