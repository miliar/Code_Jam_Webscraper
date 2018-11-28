def solve(n,k):
    d={}
    d[n]=1
    
    while 1:
        maxd=max(d)
        nummaxd=d[maxd]
        if nummaxd>=k:
            if not maxd%2:
                return (maxd/2,max(maxd/2-1,0))
            else:
                return (maxd/2,maxd/2)
        else:
            del(d[maxd])
            if not maxd%2:
                if maxd/2 in d:
                    d[maxd/2]+=nummaxd
                else:
                    d[maxd/2]=nummaxd
                if maxd/2-1 in d:
                    d[maxd/2-1]+=nummaxd
                else:
                    d[maxd/2-1]=nummaxd
            else:
                if maxd/2 in d:
                    d[maxd/2]+=2*nummaxd
                else:
                    d[maxd/2]=2*nummaxd
            k-=nummaxd
            #print k,d
        if k<0:
            print 'error'
            return
        
def go(fn):
    f=open(fn)
    cases=int(f.readline())
    for c in range(1,cases+1):
        n,k=[int(x) for x in f.readline().split()]
        r1,r2=solve(n,k)
        print 'Case #%d: %d %d'%(c,r1,r2)
    f.close()
              
go('C-large.in')
