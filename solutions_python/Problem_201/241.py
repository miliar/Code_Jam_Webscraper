t = int(raw_input())
for i in xrange(1, t + 1):
    N,K=[int(k) for k in raw_input().split(" ")]
    nbl=K
    d={}
    d[N]=1
    while nbl>0:
        p=max(d.keys())
        np=d[p]
        nbl-=np
        n1 = (p-1)/2
        n2=p-1-n1
        del d[p]
        if n1 not in d:
            d[n1]=0
        d[n1]+=np
        if n2 not in d:
            d[n2]=0
        d[n2]+=np  
        res=n2,n1
 #       print n1,n2,nbl,p,d,np
          
    
    print "Case #{}: {} {}".format(i,res[0],res[1])
