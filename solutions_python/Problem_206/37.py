

#return the point of crossing of two horses (might be in the past) K1 < K2
def cross_point(K1, V1, K2, V2):
    if V1 == V2:
        return (float('inf'), float('inf'))

    return (K1 + V1 * (K1 - K2) / (V2 - V1)), ((K1 - K2) / (V2 - V1))



def algorithm(D, N, R):
    # Ki, Si
    R = sorted([(p[0],p[1]) for p in R])

    KN,VN = R[-1]
    interval_list = [(0,KN,VN)]

    for i in reversed(range(N-1)):
        ki, vi = R[i]
        l2 = []
        for (deb, k, v) in interval_list:
            c, t = cross_point(ki,vi,k,v)
            if t <= 0 or c >= D:
                pass
            elif t <= deb:
                l2.append((deb, k, v))
            else:
                l2.append((t, k, v))
                l2.append((0, ki, vi))
                break
        if len(l2) == 0:
            interval_list = [(0, ki, vi)]
        else:
            interval_list = l2.copy()
    r,kfin, vfin = interval_list[0]
    tfin = (D - kfin)/vfin
    return D/tfin


T = int(input())

for i in range(T):
    D, N = [int(x) for x in input().split(' ')]
    R = [[int(x) for x in input().split(' ')] for _ in range(N)]
    print("Case #%d: %f" % (i+1, algorithm(D,N,R)))
