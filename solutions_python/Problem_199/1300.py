def flips(a,n,k):
    s=[]
    for i in range(n):
        s.append(0)
    Sum=0
    Ans=0
    for i in range(n):
        s[i]=(a[i]+Sum)%2!=1
        if i>=k-1:
            Sum+=s[i]-s[i-k+1]
        else:
            Sum+=s[i]
        Ans+=s[i]
        if i>n-k and s[i]!=0:
            return -1
    return Ans

tt=int(input())
for t in range(1,tt+1):
    [l,k]=input().split()
    k=int(k)
    d={'+':1,'-':0}
    s=[]
    for i in l:
        s.append(d[i])
    ans=flips(s,len(s),k)
    if ans==-1:
        print("Case #"+str(t)+":","IMPOSSIBLE")
    else:
        print("Case #" + str(t) + ":",ans)
