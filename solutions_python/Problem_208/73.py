def show(tab):
    print('[')
    for t in tab:
        print(t)
    print(']')
T = int(input())
for t in range(1,T+1):
    n,q = [int(s) for s in input().split(' ')]
    E = []
    S = []
    for i in range(n):
        ei,si = [int(s) for s in input().split(' ')]
        E.append(ei)
        S.append(si)
    d = []
    for i in range(n):
        d.append([int(s) for s in input().split(' ')])
    U =[]
    V=[]
    for i in range(q):
        u,v = [int(s) for s in input().split(' ')]
        U.append(u-1)
        V.append(v-1)

    for i in range(n):
        for j in range(n):
            if d[i][j]<0:
                d[i][j]=2000000000000000

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]


    #show(time)
    result = ''
    for i in range(q):
        u = U[i]
        v = V[i]
        time =[2000000000000000 for j in range(n)]
        time[u]=0
        for m in range(n):
            for k in range(n):
                for j in range(n):
                    if d[j][k]<=E[j] and time[j]+d[j][k]/S[j] < time[k]:
                        time[k]=time[j]+d[j][k]/S[j]
                        #show(time)
        result += str(time[v])+ ' '


    print('Case #{}: {}'.format(t,result))
