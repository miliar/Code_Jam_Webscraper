import math

def _get_max(K, sas, first=True):
    if K == 0:
        return 0
    if len(sas) == K:
        sa = 0.0
        if first:
            sa = sas[0][0]
        if len(sas)>1:
            temp = map(lambda x: x[1], sas)
            sa += reduce(lambda x,y: x+y, temp)
        else:
            sa += sas[0][1]
        return sa
    sa = (sas[0][1] + sas[0][0]) if first else sas[0][1]
    return max(sa+_get_max(K-1, sas[1:], False), _get_max(K, sas[1:], first))

def get_max_sa(N, K, panc):
    sas = map(lambda p: ((p[0]**2.0), 2.0*p[0]*p[1]), panc)
    sas.sort(key=lambda p: -p[0])
    return math.pi*_get_max(K, sas)

if __name__ == "__main__":
    t = int(raw_input().strip())
    for tno in range(0, t):
        N, K = map(int, raw_input().strip().split(' '))
        panc = []
        for _ in range(0, N):
            r, h = map(int, raw_input().strip().split(' '))
            panc.append((r, h))
        ans = get_max_sa(N, K, panc)
        print "Case #%d: %0.9f" % ( tno + 1, ans )
