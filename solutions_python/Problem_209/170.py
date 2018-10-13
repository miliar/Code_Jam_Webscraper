import math
def solve():
    N, K = map(int, raw_input().split())
    R = []
    H = []
    P = []
    for i in range(N):
        r, h = map(int, raw_input().split())
        R.append(r)
        H.append(h)
        P.append((h*r, r, h))

    P = sorted(P)[::-1]
    best = 0.
    for i, p in enumerate(P):
        # maximize sum, allow only pancakes with smaller or equal radii
        (pcoat, pr, ph) = p
        need = K-1
        coats = [pcoat]
        for j, (coat, r, h) in enumerate(P):
            if i == j:
                continue
            if need == 0:
                break
            if r <= pr:
                need -= 1
                coats.append(coat)
        if need == 0:
            coats = sum(sorted(coats))
            best = max(best, coats + (pr*pr/2.))
    return 2*math.pi*best



T = int(raw_input())
for t in range(1, T+1):
    print "Case #{}: {}".format(t, solve())
