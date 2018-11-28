import psyco
psyco.full()
def findT(q,k):
    i=0
    l=len(q)
    rt=0
    cost=0
    ft=[(0,0) for x in range(l)]
    while True:
        lr=0
        cn=0
        while lr+q[i]<=k and cn<l:
            lr+=q[i]
            i+=1
            cn+=1
            if i==l:
                i=0
            
        cost+=lr
        rt+=1
        if ft[i][0]==0:
            ft[i]=(cost,rt)
        else:
            modcost,modr=ft[i]
            rt=rt-modr
            cost=cost-modcost
            spos=i
            break
        
    return rt,cost,modr,modcost,spos

def runForR(q,k,R,spos):
    i=spos
    l=len(q)
    rt=0
    cost=0
    while True:
        lr=0
        cn=0
        while lr+q[i]<=k and cn<l:
            lr+=q[i]
            i+=1
            cn+=1
            if i==l:
                i=0
        cost+=lr
        rt+=1
        if rt==R:
            break
    return cost
print 'start'
fin=file('c.in')
fout=file('c.out','w')
T=int(fin.readline().strip())
for t in range(T):
    R,k,N=[int(x) for x in fin.readline().strip().split()]
    que=[int(x) for x in fin.readline().strip().split()]
    rt,cost,modr,modcost,spos=findT(que, k)
    if R>=rt+modr:
        R-=modr
        tcost=modcost
        time,modr=divmod(R,rt)
        if modr>0:
            costmod=runForR(que,k,modr,spos)
        else:
            costmod=0
        tcost=tcost+cost*time+costmod
    else:
        tcost=runForR(que,k,R,0)
    
    #tcost=runForR(que,k,R)
    rst='Case #%d: %d\n'%(t+1,tcost)
    #print rst,
    fout.write(rst)
fout.close()
print 'ok'
