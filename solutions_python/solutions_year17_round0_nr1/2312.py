for i in xrange(1,input()+1):
    s,p=raw_input().strip().split()
    l = len(s)
    arr = [0]*l
    f=0
    p=int(p)
    for j in xrange(l-p+1):
        if ((s[j]=='-') ^ arr[j]):
            for k in xrange(j,j+p):
                arr[k]^=1
            f+=1
    for j in xrange(l-p,l):
        if ((s[j]=='-') ^ arr[j]):
            f=-1
    if f>=0:
        print "Case #%d: %d"%(i,f)
    else:
        print "Case #%d: IMPOSSIBLE"%(i)
