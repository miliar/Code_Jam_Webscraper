for t in range(int(raw_input())):
    s,k=raw_input().split()
    k=int(k)
    l=len(s)
    s=list(s)
    ans=0
    for i in range(l-k+1):
        if s[i]=='+':
            continue
        ans+=1
        for j in range(i,i+k):
            if s[j]=='-':
                s[j]='+'
            else:
                s[j]='-'
    for i in range(l):
        if s[i]!='+':
            ans=-1
    if ans== -1:
        print "Case #%d: %s" %(t+1,"IMPOSSIBLE")
    else:
        print "Case #%d: %d" %(t+1,ans)

