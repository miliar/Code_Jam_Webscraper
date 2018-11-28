def doit(D, KS):
    Sas = []
    for KSi in KS:
        (Ki, Si) = KSi
        restDi = D - Ki
        Ti = restDi/Si
        Sas.append(D/Ti)
    #if len(KS) > 1:
    #    (K1, S1) = KS[1]
    #    restD1 = D - K1
    #    T1 = restD1/S1
    #    if K1 < K0 and T1 < T0:
    #        # H1 will overtake H0, slow down
    #        x = (K0-K1)/(S1-S0)
    #        y = S0*x + K0
    #        #print('  H1 reaches H0 after {}h at {}km'.format(x,y))
    #    Sa = D/T1
    #    Sas.append(Sa)
    return min(Sas)

T = int(input())
for t in range(1, T+1):
    [D, N] = [int(x) for x in input().split(' ')]
    KS = []
    for i in range(1, N+1):
        [Ki, Si] = [int(x) for x in input().split(' ')]
        KS.append((Ki,Si))
    # sort by ascending S, then by descending K
    KS.sort(key=lambda tup: (tup[1], -tup[0]))
    #print('Case #{}: {} {}'.format(t, D, KS))
    Sa = doit(D, KS)
    #if len(KS)>1:
        #print('      {}: Sa = {}'.format(t, Sa))
    print('Case #{}: {}'.format(t, Sa))
    #print()

