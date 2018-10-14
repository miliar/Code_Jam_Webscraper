#Henry Maltby
#Code Jam 2017

import math

def pony_express(limits, speeds, dists, starts, ends):
    """
    Assume cities in a line and only one test (first to last).
    """
    N = len(limits)
    times = [[math.inf] * N for i in range(N)]
    times[0][0] = 0
    ds = [0] + [dists[i-1][i] for i in range(1, N)]
    for i in range(1, N):
        ds[i] += ds[i - 1]
    for i in range(N):
        for j in range(i):
            how_far = ds[i] - ds[j]
            if limits[j] >= how_far:
                times[i][j] = times[j][j] + (how_far / speeds[j])
        times[i][i] = min(times[i])
    return [str(times[-1][-1])]

def C():
    """
    Runs the program as dictated in problem spec.
    """
    f = open('C-small-attempt0.in')
    g = open('C-small-attempt0.out', 'w')

    T = int(f.readline())
    for i in range(T):
        N, Q = [int(x) for x in f.readline().strip().split(' ')]
        E, S = [], []
        for j in range(N):
            e, s = [int(x) for x in f.readline().strip().split(' ')]
            E.append(e)
            S.append(s)
        D = []
        for j in range(N):
            D.append([int(x) for x in f.readline().strip().split(' ')])
        U, V = [], []
        for j in range(Q):
            u, v = [int(x) for x in f.readline().strip().split(' ')]
            U.append(u)
            V.append(v)
        ans = pony_express(E, S, D, U, V)
        g.write("Case #" + str(i + 1) + ": " + " ".join(ans))
        if i != T - 1:
            g.write("\n")

C()
