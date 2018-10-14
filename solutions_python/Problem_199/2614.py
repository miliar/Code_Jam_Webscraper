t = int(raw_input())
for i in xrange(t):
    s,k = raw_input().strip().split()
    
    k=int(k)
    li=list(s)
    n=len(li)
    
    chk=[]
    for j in xrange(n):
        chk.append('+')
    
    j=0
    ans=0
   
    while(j<=n-k):
        if li[j]=='-':
            temp=j
            while(temp<j+k):
                if li[temp]=='-':
                    li[temp]='+'
                else:
                    li[temp]='-'
                temp+=1
            ans+=1
        j+=1

    
    if cmp(li,chk):
        print "Case #{}: {}".format(i+1,"IMPOSSIBLE")
    else:
        print "Case #{}: {}".format(i+1,ans)
        
    