import sys

f = open(sys.argv[1])
T = int(f.readline())
for t in range(T):
    N = int(f.readline())
    vines = [map(int, f.readline().split()) for v in range(N)]
    vines += [[int(f.readline()), 0]]
    best = [vines[0][0]] + [-1] * N
    for i in range(1, N + 1):
        for j in range(i):
            dist = vines[i][0] - vines[j][0]
            if best[j] >= dist:
                eff_len = min(vines[i][1], dist)
                best[i] = max(best[i], eff_len)
        if best[i] == -1:
            break
    print "Case #%d:" % (t + 1), "YES" if best[-1] >= 0 else "NO"
