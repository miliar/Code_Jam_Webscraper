def genlist(n):
    l = []
    for i in range(n):        
        l.append((1<<i)-1)
    return l

def main (argv):
    ifname=argv[0]
    ofname=argv[1]
    ifp=open(ifname,'rU')
    ofp=open(ofname,'wb')
    iifp=iter(ifp)
    fstl=iifp.next()
    num=int(fstl)
    nl = genlist(31)

    for i in range(num):
        l=iifp.next().strip()
        d=l.split()
        n,k=int(d[0]),int(d[1])
        upperbound= nl[n]
        if k & upperbound == upperbound:
            ofp.write("Case #%d: %s\n" % (i+1,'ON'))
        else:
            ofp.write("Case #%d: %s\n" % (i+1,'OFF'))
    ifp.close()
    ofp.close()

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
        
