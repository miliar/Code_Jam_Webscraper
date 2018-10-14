def con(L, m, M):
    target = []
    for n in xrange(m, M+1):
        if n not in L:
            target.append(n)
    return target

def solve_cr(sum, dif):
    return [(sum+dif)/2, (sum-dif)/2]

for i in xrange(1, input()+1):
    l = raw_input().split()
    X, T = [], []
    for j in xrange(int(l[1])):
        s = raw_input().split()
        x, y = int(s[1]), int(s[2])
        if s[0] != '+':
            X.append([x, y])
        if s[0] != 'x':
            T.append([x, y])
    cp_X, cp_T = X[:], T[:]
    N = int(l[0])
    x_lis, y_lis = con([p[0] for p in X], 1, N), con([p[1] for p in X], 1, N)
    sum_lis, dif_lis = con([p[0]+p[1] for p in T], 2, N*2), con([p[0]-p[1] for p in T], -N+1, N-1)
    
    for n in xrange(len(x_lis)):
        X.append([x_lis[n], y_lis[n]])
    delta = len(x_lis)
    '''
    for s in sum_lis:
        for d in dif_lis:
            if (s+d) % 2 == 0:
                solve = solve_cr(s, d)
                if N >= solve[0] > 0 and N >= solve[1] > 0:
                    T.append(solve)
                    dif_lis.remove(d)
                    delta += 1
                    break
                    '''
    for d in xrange(N-1, -1, -1):
        if d in dif_lis:
            for s in sum_lis:
                if (s+d) % 2 == 0:
                    solve = solve_cr(s, d)
                    if N >= solve[0] > 0 and N >= solve[1] > 0:
                        T.append(solve)
                        sum_lis.remove(s)
                        delta += 1
                        break
        if d==0:
            break
        if -d in dif_lis:
            for s in sum_lis:
                if (s-d) % 2 == 0:
                    solve = solve_cr(s, -d)
                    if N >= solve[0] > 0 and N >= solve[1] > 0:
                        T.append(solve)
                        sum_lis.remove(s)
                        delta += 1
                        break
                
        
    point = len(X) + len(T)
    O_add = []
    for p in X:
        if p in T:
            t, x = p in cp_T, p in cp_X
            if not (t and x):
                delta -= 1 - t - x
                O_add.append(p)
                X.remove(p)
                T.remove(p)
        
    print "Case #%d: %d %d"%(i, point, delta)
    for o in O_add:
        print 'o', o[0], o[1]
    for t in T:
        if t not in cp_T:
            print '+', t[0], t[1]
    for x in X:
        if x not in cp_X:
            print 'x', x[0], x[1]