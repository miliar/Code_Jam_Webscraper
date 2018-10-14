from decimal import *
INF=10000000000000
TMAX= Decimal(120000./0.0000001)
EPS = Decimal(1e-16)
tcas=int(raw_input())

def ccw(a,b):
    return a[0]*b[1]-b[0]*a[1]

def above_below(pt,vecs):
    x,y=Decimal('0'),Decimal('0')
    for i in vecs:
        nx = x+i[0]
        ny = y+i[1]
        if(nx>=pt[0]):
            v=(pt[0]-x,pt[1]-y)
            sgn = ccw(v,i)
            #print 'n',nx,sgn,sgn/(i[0]+i[1])/(v[0]+v[1])
            if(sgn>Decimal('0')):
                return -1
            elif(-(v[0]+v[1])*EPS<sgn<(v[0]+v[1])*EPS):
                return 2
            else:
                return 1
        x=nx
        y=ny
    return False
def gs(x):
    a,b=0,0
    for i in x:
        a+=i[0]
        b+=i[1]
    return (a,b)

def dedup(rc):
    nvecs={}
    for i in rc:
        nvecs[i[1]]=[]
    for i in rc:
        nvecs[i[1]].append(i[0])
    res=[]
    for i in nvecs:
        res.append((i,sum(nvecs[i])))
    return res

def cando(probe,n,rc,v,x):
    en = v*x
    vecs = [(i[1],(i[0]*probe,i[0]*probe*i[1])) for i in rc]
    nvecs={}
    for i in vecs:
        nvecs[i[0]]=[]
    for i in vecs:
        nvecs[i[0]].append(i[1])
    act = []
    for i in nvecs:
        act.append(gs(nvecs[i]))
    if(len(act)==1):
        return v<=act[0][0]
    p = (v,en)
    bot= above_below(p,act)
    act.reverse()
    top = above_below(p,act)
    if(bot==False or top==False):
        return False
    if(bot==2 or top==2):
        return True
    return ((bot+top)==0)

for cas in xrange(1,tcas+1):
    s=raw_input().split()
    n=int(s[0])
    v=Decimal(s[1])
    x=Decimal(s[2])
    rc=[map(Decimal,raw_input().split()) for i in xrange(n)]
    rc=dedup(rc)
    #print rc
    rc.sort()
    ans=0
    if(rc[0][0]==x):
        ans=v/rc[0][1]
    elif(rc[-1][0]==x):
        ans=v/rc[-1][1]
    elif(x<rc[0][0] or x>rc[-1][0]):
        #print rc[0][0],rc[-1][0]
        ans="IMPOSSIBLE"
    else:
        rc=[(i[1],i[0]) for i in rc]
        lo = EPS 
        hi = TMAX
        while(hi-lo>EPS and hi-lo>EPS*(hi-lo)):
            #print hi,lo
            probe = (hi+lo)/2
            if(cando(probe,n,rc,v,x)):
                hi=probe
            else:
                lo=probe
        ans = (hi+lo)/2
        if(ans>TMAX-EPS):
            ans="IMPOSSIBLE"
    print "Case #{}: {}".format(cas,ans)
