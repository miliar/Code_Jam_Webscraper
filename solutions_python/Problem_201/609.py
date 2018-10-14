import numpy as np
t=int(raw_input())
for i in xrange(1, t+1):
    n, k= [int(x) for x in raw_input().split()]
    if k==1:
        y, z= n/2, n-1-n/2
    else:
        q =[]
#        l =int(np.floor(np.log2(k)))
        l=0
        while 2**l < k:
            l+=1
        if 2**l > k:
            l-=1
#        print 'l=', l
        q=[[1, n-1-n/2], [1, n/2]]
        if n%2 ==1:
            q=[[0, n/2-1],[2, n/2]]
        for j in xrange(1, l):
            a, kk=q[0]
            b, kk1=q[1]
            q.pop(0)
            q.pop(0)
            if kk1 % 2==0:
                q=[[2*a+b, kk1/2 -1], [b, kk1/2]]
            else:
                q=[[a, kk1/2 -1], [a+2*b, kk1/2]] 
        c=k-2**(l)+1
        a, kk=q[0]
        b, kk1=q[1]
        if b >= c:
            y, z= kk1/2, kk1-1-kk1/2
        else:
            y, z= kk/2, kk-1-kk/2
#    q.pop(0)
#    q.pop(0)
    print "Case #%d: %d %d" % (i, y, z)
 