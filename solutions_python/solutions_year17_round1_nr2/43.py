from math import ceil
for tc in xrange(1,1+input()):
    print "Case #%d:"%tc,
    n,p=map(int,raw_input().strip().split())
    r = map(int,raw_input().strip().split())
    q = []
    for i in xrange(n):
        q.append(map(float,raw_input().strip().split()))
        for j in xrange(p):
            q[i][j]/=r[i]
        q[i].sort()
    point=[0]*n
    answer=0
    while max(point)<p:
        tarr=[q[i][point[i]] for i in xrange(n)]
        x=min(tarr)
        y=max(tarr)
        if int(x*10/9)*11/10.0<=0:
            point[tarr.index(x)]+=1
        elif int(x*10/9)*11/10.0 >=y:
            answer+=1
            for i in xrange(n):
                point[i]+=1
        else:
            point[tarr.index(x)]+=1
    print answer
        
        
