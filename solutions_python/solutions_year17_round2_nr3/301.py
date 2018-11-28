from fractions import Fraction
t = int(input())
ip = lambda : [int(i) for i in input().split()]
for i in range(1, t+1):
    N, Q = ip()
    H = []
    d = []
    for j in range(N):
        H.append(tuple(ip()))
    for j in range(N):
        nxt = ip()
        if j+1 < N:
            d.append(nxt[j+1])
    for j in range(Q):
        U, V = ip()
        t = [-1 for _ in range(N)]
        t[0] = 0
        for k in range(N-1):
            hl, hs = H[k][0], H[k][1]
            l = k + 1
            cd = 0
            while l < N and hl >= d[l - 1]:
                hl -= d[l-1]
                cd += d[l-1]
                if t[l] == -1 or t[l] > t[k] + Fraction(cd, hs):
                    t[l] = t[k] + Fraction(cd, hs)
                l += 1
        print('Case #%d: %f'%(i, float(t[N-1])))

