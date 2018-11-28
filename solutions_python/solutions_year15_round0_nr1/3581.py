t=int(raw_input())
for T in xrange(t):
    M,s=[x for x in raw_input().split()]
    M=int(M)
    s=list(int(x) for x in s)
    sum=s[0]
    count=0
    for i in xrange(1,M+1):
        if s[i]!=0 and sum<i:
            count+=(i-sum)
            sum+=count+s[i]
        else:
            sum+=s[i]
    print 'Case #'+str(T+1)+': '+str(count)
