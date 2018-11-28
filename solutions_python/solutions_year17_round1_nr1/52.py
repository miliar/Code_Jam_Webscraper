for i in xrange(1,1+input()):
    r,c=map(int,raw_input().strip().split())
    ck=[]
    f=0
    for j in xrange(r):
        ck.append(list(raw_input()))
        if ck[-1]==['?']*c:
            if f==0:
                continue
            else:
                ck[-1]=ck[-2]
        else:
            ind = 0
            for k in xrange(c):
                if ck[-1][k]!='?':
                    ind=k
                    break
            ck[-1]=ck[-1][ind:ind+1]*ind+ck[-1][ind:]
            for k in xrange(ind+1,c):
                if ck[-1][k]=='?':
                    ck[-1][k]=ck[-1][k-1]
            if f==0:
                x=ck[-1]
                ck=[]
                for k in xrange(j+1):
                    ck.append(x)
            f=1
    print "Case #%d:"%i
    for j in xrange(r):
        print ''.join(ck[j])
