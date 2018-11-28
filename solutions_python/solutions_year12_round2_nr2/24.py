import sys
import cStringIO as StringIO

#f = file('/Users/larsr/Downloads/B-small-attempt0.in')
f = file('/Users/larsr/Downloads/B-large (1).in')
#with sys.stdin as f:

ff= StringIO.StringIO("""\
4
200 1 2
250 233
180 100
100 3 3
500 500 500
500 500 600
500 140 1000
10 10 10
10 10 490
10 10 10
100 3 3
500 100 500
100 100 500
500 500 500
10 10 10
10 10 10
10 10 10
100 2 2
1000 1000
1000 1000
100 900
900 100
""")


MAXTIME=10**6
def earliest_enter_time(c_old,f_old,c_new,f_new,water):
    if c_new-f_new<50: return MAXTIME
    if c_new-f_old<50: return MAXTIME
    if c_old-f_new<50: return MAXTIME
    if c_new - water>50: return 0.
    return (50-(c_new - water))/10.

T = int(f.readline())
for case in range(1,T+1):
    print 'Case #%d:' % case,
    H,N,M = [int(x) for x in f.readline().strip().split()]
    #print 'N,M=',N,M
    C=[]
    for i in range(N):
        C.append([int(x) for x in f.readline().strip().split()])
    F=[]
    for i in range(N):
        F.append([int(x) for x in f.readline().strip().split()])
    X = []
    for i in range(N):
        X.append([MAXTIME]*M)  # the earliest time we arrive to a grid cell
    #print H,N,M,
    X[0][0]=0.

    def neighbors(n,m):
        neigh=[]
        for dn,dm in [(-1,0),(1,0),(0,-1),(0,1)]:
            if 0<=n+dn<N and 0<=m+dm<M:
                neigh.append((n+dn,m+dm))
        return neigh

    done = False
    while not done:
        done = True
        for n in range(N):
            for m in range(M):
                t = X[n][m]
                if t < MAXTIME:
                    for n1,m1 in neighbors(n,m):
                        #print 'checking neighbor',(n1,m1)
                        t1 = X[n1][m1]
                        t_enter = earliest_enter_time(C[n][m],F[n][m],C[n1][m1],F[n1][m1],H)
                        #print 'earliest enter from',(n,m),'to',(n1,m1),'=',t_enter
                        if t < t1:
                            tt = max(t_enter,t)
                            #print 'water while moving',H-10.*tt - F[n][m]
                            if tt == 0: 
                                cost = 0
                            else:
                                water_depth = H-10.*tt - F[n][m]
                                if water_depth >= 20:
                                    cost = 1
                                else:
                                    cost = 10

                            t1_new = max(min(t1, tt+cost),t_enter)

                            if t1_new < t1:
                                X[n1][m1] = t1_new
                                done = False
                    
    #print 'done',X[N-1][M-1],X
    print X[N-1][M-1]

