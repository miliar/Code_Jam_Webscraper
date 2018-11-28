import sys
import numpy as np

data = sys.stdin.readlines()
t = int(data[0])
l = 1
for i in range(t):
    print "Case #%d:" % (i+1),

    d = data[l].split()
    l += 1

    N = int(d[0])
    S = [0] * N
    E = [0] * N
    for j in range(N):
        d = data[l].split()
        l += 1

        E[j] = float(d[0])
        S[j] = float(d[1])

    D = [0] * (N-1)
    for j in range(N):
        d = data[l].split()
        l += 1

        if j != N-1:
            D[j] = int(d[j+1])

    l += 1

    i_s = 0
    # t, s, e tuplets
    sims = [[0.0, 1.0, 0.0]]

    for k in range(N-1):
        # Add this town's horse
        t = [s[0] for s in sims]
        i_m = np.argmin(t)
        s_m = sims[i_m]
        sims.append([s_m[0], S[k], E[k]])

        # Move horses to next town
        for h in range(len(sims)):
            sims[h][0] += D[k] / sims[h][1]
            sims[h][2] -= D[k]

        # Also remove any that can't make it
        sims = [s for s in sims if not s[2] < 0]

    t = [s[0] for s in sims]
    print "%.6f" % min(t)

