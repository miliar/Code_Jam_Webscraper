import sys

def sim_stalls(K, N):
    stalls = [0]*(N+2)
    stalls[0] = stalls[-1] = 1
    
    Ls = list(range(N+2))
    Rs = list(range(N+2))[::-1]
    
    lowest_unocc = 1
    
    for k in range(K):
        ns = None
        bestmin = None
        bestmax = None
        for i in range(1, N+1):
            if Ls[i] != 0 and Rs[i] != 0:
                ns = 1
                bestmin = min(Ls[ns], Rs[ns])
                bestmax = max(Ls[ns], Rs[ns])
                break
        for i in range(ns+1, N+1):
            minLR = min(Ls[i], Rs[i])
            maxLR = max(Ls[i], Rs[i])
            if minLR > bestmin:
                ns = i
                bestmin, bestmax = minLR, maxLR
            elif minLR == bestmin and maxLR > bestmax:
                ns = i
                bestmin, bestmax = minLR, maxLR
        for i in range(ns, N+2):
            if Ls[i] == 0:
                break
            Ls[i] = i-ns
        for i in range(ns, -1, -1):
            if Rs[i] == 0:
                break
            Rs[i] = ns - i

    return bestmax - 1, bestmin - 1


with open(sys.argv[1]) as inp, open(sys.argv[2], "w") as out:
    next(inp)
    for i, l in enumerate(inp, start=1):
        N, K = map(int, l.split())

        y, z = sim_stalls(K, N)

        print(f"Case #{i}: {y} {z}", file=out)