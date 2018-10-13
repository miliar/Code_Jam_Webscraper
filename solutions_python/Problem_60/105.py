#!/usr/bin/python


for case in range(input()):
    N, K, B, T = [int(x) for x in raw_input().split()]
    X = [int(x) for x in raw_input().split()]
    V = [int(x) for x in raw_input().split()]

    t_opt = [float(B - x) / v for (x, v) in zip(X, V)]

    out = "IMPOSSIBLE"
    candidate = [t <= T for t in t_opt]
    if len([c for c in candidate if c]) >= K:
        blockers = [0 for x in range(N)]
        for i in range(N):
            blocks = 0
            if not candidate[i]:
                continue
            for j in range(i + 1, N):
                r = V[i] - V[j]
                d = X[j] - X[i]
                if r <= 0:
                    continue
                if not candidate[j]:
                    blocks = blocks + 1
            blockers[i] = blocks
        res = [b for (i, b) in enumerate(blockers) if candidate[i]]
        res.sort()
        out = sum(res[:K])

    print("Case #%s: %s" % (case + 1, out))

