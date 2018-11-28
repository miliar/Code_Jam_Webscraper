def gettotal(l,n,k,r):
    nl=[None]*n
    o = 0
    t_n = 0
    t_s = 0
    t_complete = False
    s=0
    while r > 0:
        if nl[o] is None:
            no,ss=getnext(l,n,o,k)
            #print o,no,ss
            nl[o]=((no,ss),(s,r))
            s+=ss
            o=no
            r-=1
        elif t_complete == False:
            #print "found circle entry at %d"%o
            t_complete=True
            t_n=nl[o][1][1]-r
            t_s=s-nl[o][1][0]
            #print t_n,t_s,nl[o],r
            s+=r/t_n*t_s
            r=r%t_n
        else:
            s+=nl[o][0][1]
            o=nl[o][0][0]
            r-=1
    return s

def getnext(l,n,o,k):
    sn=k
    oo = o
    while sn >= l[o]:
        sn-=l[o]
        o=(o+1)%n
        if o==oo:
            break
    return o,k-sn

def main (argv):
    ifname=argv[0]
    ofname=argv[1]
    ifp=open(ifname,'rU')
    ofp=open(ofname,'wb')
    iifp=iter(ifp)
    fstl=iifp.next()
    num=int(fstl)

    for i in range(num):
        l1=iifp.next().strip()
        l2=iifp.next().strip()
        d=l1.split()
        r,k,n=int(d[0]),long(d[1]),int(d[2])
        l=map(int,l2.split())
        ofp.write("Case #%d: %d\n" % (i+1, gettotal(l,n,k,r)))
    ifp.close()
    ofp.close()

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
