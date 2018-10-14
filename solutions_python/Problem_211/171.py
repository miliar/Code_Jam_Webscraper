T = int(raw_input())

for t in range(1, T+1):
    N, K = map(int, raw_input().split())
    U = float(raw_input())
    P = map(float, raw_input().split())
    
    # when N = K:
    
    P = sorted(P)
    
    P_N = dict()
    for p in P:
        if p not in P_N:
            P_N[p] = 1
        else:
            P_N[p] += 1
    # print min(P_N.keys())
    
    while U > 0:
        # print P_N
        if len(P_N) < 2:
            p = min(P_N.keys())
            n = P_N[p]
            p_ = p + U/n
            del P_N[p]
            P_N[p_] = n
            U = 0
            # print U, P_N
        else:
            p, p2 = sorted(P_N.keys())[:2]
            n = P_N[p]
            delta = min(U/n, p2 - p)
            p_ = p + delta
            del P_N[p]
            if p_ not in P_N:
                P_N[p_] = n
            else:
                P_N[p_] += n
            U -= delta * n
            # print U, P_N

    ans = 1.0
    for p, n in P_N.items():
        ans *= p**n
    
    print 'Case #%d: %f' % (t, ans)
