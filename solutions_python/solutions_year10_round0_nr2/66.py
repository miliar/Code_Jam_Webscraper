def gcd(a,b):
    if a<b:
        a1=a
        a=b
        b=a1
    while b >0:
        a1=a%b
        a=b
        b=a1
    return a

def multiplegcd(l):
    g=l[0]
    for e in l[1:]:
        g=gcd(g,e)
    return g

def getT(n,l):
    nl=[]
    l.sort()
    for i in range(n-1):
        nl.append(l[i+1]-l[i])
    g=multiplegcd(nl)
    t=(g-(l[0]%g))%g
    return t

def main (argv):
    ifname=argv[0]
    ofname=argv[1]
    ifp=open(ifname,'rU')
    ofp=open(ofname,'wb')
    iifp=iter(ifp)
    fstl=iifp.next()
    num=int(fstl)

    for i in range(num):
        l=iifp.next().strip()
        d=l.split()
        n=int(d[0])
        ofp.write("Case #%d: %d\n" % (i+1, getT(n,map(long,d[1:]))))
    ifp.close()
    ofp.close()

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
