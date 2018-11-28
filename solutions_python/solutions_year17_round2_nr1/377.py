from fractions import Fraction

t = int(input())
ip = lambda: map(int, input().split())
for i in range(1, t+1):
    D, N = ip()
    L = []
    for j in range(N):
        L.append(tuple(ip()))
    L.sort(key=lambda a: a[0], reverse=True)
    f = [Fraction(0,1) for _ in range(N)]
    f[0] = Fraction(D - L[0][0], L[0][1])
    prevS, prevT, prevD = L[0][1] ,f[0], L[0][0]
    for j in range(1, N):
        d =  prevD - L[j][0]
        s2 = L[j][1]
        s1 = prevS
        if s2 - s1 <= 0 or d > (s2 - s1)*prevT:
            f[j] = Fraction(D - L[j][0], s2) 
            prevT = f[j]
            prevS = s2
            prevD = L[j][0]
        else:
            f[j] = prevT
    T = max(f)
    ans = D/T
    print('Case #%d: %f'%(i,float(ans)))

       

