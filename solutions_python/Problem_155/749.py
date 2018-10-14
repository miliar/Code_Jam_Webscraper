t=input()
for i in range(t):
    n,s=raw_input().split()
    n=int(n)
    s=map(int,s)
    pers=s[0]
    ans=0
    if s[0]==0:
        pers+=1
        ans+=1
    for x in range(1,n+1):
        if pers>=x:
            pers+=s[x]
        else:
            ans+=x-pers
            pers=x+s[x]
    print "Case #"+str(i+1)+": "+str(ans)
