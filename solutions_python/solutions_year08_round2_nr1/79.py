def solve():
    f = open('A-small.in')
    g = open('A.out','w')
    N = int(f.readline())
    for i in range(N):
        n, A, B, C, D, x0, y0, M = map(int,f.readline().split())
        ret = 0
        x = [x0]
        y = [y0]
        X, Y = x0, y0
        for k in range(n-1):
            X = (A * X + B) % M
            Y = (C * Y + D) % M
            x += [X]
            y += [Y]
        for j1 in range(n):
            for j2 in range(n):
                for j3 in range(n):
                    if j1>=j2 or j2>=j3 : continue
                    if (x[j1]+x[j2]+x[j3])%3==0 and (y[j1]+y[j2]+y[j3])%3==0 : ret+=1
        g.write('Case #'+str(i+1)+': '+str(ret)+'\n')
    g.close()
solve()