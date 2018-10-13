# Linguo entry for Problem A in 2015 Google Code Jam Round 3 'The Battle for Seattle'

def reader(inFile):
    (N, D) = inFile.getInts()
    print N
    (S0, As, Cs, Rs) = inFile.getInts()
    (M0, Am, Cm, Rm) = inFile.getInts()
    S = [S0]
    M = [M0]
    for i in xrange(N - 1):
        S.append((S[-1] * As + Cs) % Rs)
        M.append((M[-1] * Am + Cm) % Rm)
    return (N, S, [0]+[M[i] % i for i in xrange(1,N)], D)

def solver((N, S, M, D)):
    mx = [0] * N
    mn = [0] * N
    mx[0] = S[0]
    mn[0] = S[0]
    for i in xrange(1, N):
        mx[i] = max(mx[M[i]],S[i])
        mn[i] = min(mn[M[i]],S[i])
    # Employee i can still be hired with range [z, z+D] if mn[i] >= z and mx[i] <= z + D
    w = {}
    for i in xrange(N):
        if mn[i] >= mx[i] - D:
            if mx[i]-D in w:
                w[mx[i]-D] += 1
            else:
                w[mx[i]-D] = 1
            if mn[i] + 1 in w:
                w[mn[i] + 1] -= 1
            else:
                w[mn[i] + 1] = -1
    rec = 0
    tot = 0
    w = sorted([(a,b) for (a,b) in w.items()])
    for (a,b) in w:
        tot += b
        if tot >= rec:
            rec = tot
    return rec

if __name__ == "__main__":
    from GCJ import GCJ
    GCJ(reader, solver, "/Users/luke/gcj/2015/3/a/", "a").run()
