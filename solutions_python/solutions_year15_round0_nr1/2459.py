for z in xrange(int(raw_input())):
    smax,s=raw_input().split()
    smax=int(smax)
    s=map(int,list(s))
    f=0
    a=0
    slen=len(s)
    for i in range(slen):
        if(s[i]!=0):
            if(a>=i):
                a+=s[i]
            else:
                f+=(i-a)
                a=i+s[i]
    print("Case #%d: %d"%(z+1,f))                
