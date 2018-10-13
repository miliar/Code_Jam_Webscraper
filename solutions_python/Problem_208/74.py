from collections import deque

def solve(N, _, Es, Ss, Qs, dists):

    for i in range(N):
        dists[i][i] = 0

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dists[i][k] != -1 and dists[k][j] != -1:
                    new = dists[i][k] + dists[k][j]
                    if dists[i][j] == -1 or new < dists[i][j]:
                        dists[i][j] = new

    for i in range(N):
        for j in range(N):
            if dists[i][j] == -1:
                dists[i][j] = None
            elif dists[i][j] > Es[i]:
                dists[i][j] = None
            else:
                dists[i][j] = dists[i][j] / Ss[i]


    res = []
    for F, T in Qs:
        F -= 1
        T -= 1

        to_resolve = deque([F])

        best = [None] * N
        best[F] = 0

        while to_resolve:
            u = to_resolve.popleft()
            for v in range(N):
                if dists[u][v] is None:
                    continue
                new = best[u] + dists[u][v]
                if best[v] is None or new < best[v]:
                    best[v] = new
                    to_resolve.append(v)
        res.append(best[T])

    return ' '.join(map(str, res))

def read_line():
    return list(map(int, input().split(' ')))

def read_case():
    N, Q = read_line()
    ponies = [read_line() for _ in range(N)]
    Es, Ss = zip(*ponies)
    dists = [read_line() for _ in range(N)]
    Qs = [read_line() for _ in range(Q)]
    return (N, Q, Es, Ss, Qs, dists)

T = int(input())

solutions = [solve(*read_case()) for _ in range(T)]

for i, x in enumerate(solutions):
    print("Case #{}: {}". format(i+1, x))
