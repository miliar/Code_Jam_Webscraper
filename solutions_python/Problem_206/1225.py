

F = open('cruise.in2')
T = int(F.readline()[:-1])

CASE = {}
for i in range(T):
    CASE[i] = []
    
i = 0
d = -1
n = -1
for L in F:
    if d == -1:
        d,n = map(int,L[:-1].split(' '))
        CASE[i].append([d,n])
        print '>>>', d,n
    else:
        k,s = map(int,L[:-1].split(' '))
        CASE[i].append([k,s])
        print '+++', k,s
        if len(CASE[i]) == n+1:
            i += 1
            d = -1

F.close()

W = open('cruise.res2','w')
for i in range(T):
    d = float(CASE[i][0][0])
    t = 0.
    for h in CASE[i][1:]:
        t = max( t , float(d-h[0])/float(h[1]) )
    print >> W , 'Case #'+str(i+1)+': '+str( float(d)/float(t) )
W.close()
