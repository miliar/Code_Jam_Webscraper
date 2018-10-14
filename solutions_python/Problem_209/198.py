import math

T = int(raw_input())

for t in range(1, T+1):
    N, K = map(int, raw_input().split())
    R = [0] * N
    H = [0] * N
    RH = [0] * N
    for i in range(N):
        R[i], H[i] = map(int, raw_input().split())
        RH[i] = R[i] * H[i]
    
    # print R, H, RH
    # R_s = list(sorted(R))[K - 1]
    best = 0.0
    for i in range(N):
        r = R[i]
        tmp = math.pi * r**2
        RH_r = sorted([RH[j] for j in range(N) if R[j] <= r and j != i])
        if len(RH_r) + 1 < K:
            continue
        
        for j in range(K-1):
            tmp += 2*math.pi * RH_r[-(j+1)]
        tmp += 2*math.pi * RH[i]
        # tmp += 2*math.pi * (sum(RH_r[-(K-1):]) + RH[i])
        # print i, r, RH_r, tmp
        
        best = max(best, tmp)
        
    print 'Case #%d: %f' % (t, best)
