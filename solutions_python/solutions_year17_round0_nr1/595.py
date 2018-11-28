
t=int(raw_input())
for i in xrange(1, t+1):
    s, k= raw_input().split()
    k=int(k)
    n=len(s)
    ss=list(s)
 #   print ss
    ans=0
    while len(ss) >= k:
        c=0
        while  c < len(ss) and ss[c]=='+':
#            print ss[c]
            c+=1
        ss=ss[c:]
        if len(ss) >=k:
            for j in xrange(k):
                if ss[j]=='+':
                    ss[j]='-'
                else:
                    ss[j]='+'
            ans+=1
    if len(ss) > 0:
        ans=-1            
    if  ans >=0:     
        print "Case #%d: %d" % (i, ans)
    else:
        print "Case #%d: %s" % (i, 'IMPOSSIBLE')