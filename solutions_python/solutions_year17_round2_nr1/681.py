def f(D,N,K,S):
    maxt = None
    for i in range(N):
        d = D-K[i]
        t = d/S[i]
        maxt = t if maxt==None else max(t, maxt)
    return D/maxt

fin = open('al.in')
fout = open('al.out','w')
input = fin.readline
T = int(input())
for i in range(1, T+1):
    D, N = [int(x) for x in input().split(' ')]
    K, S = [], []
    for _ in range(N):
        x, y = [int(a) for a in input().split(' ')]
        K.append(x)
        S.append(y)

    r = f(D,N,K,S)
    fout.write('Case #%s: %s\n' %(i, r))