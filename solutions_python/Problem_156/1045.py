t=int(raw_input())
fp=open('a.txt','w')
for _ in xrange(1,t+1):
        n=int(raw_input())
        l=[int(x) for x in raw_input().split()]
        m=max(l)
        ans=m
        i=1
        while i<=m:
                s=i
                j=0
                while j<n:
                        if l[j]>i and l[j]%i==0:
                                s+=l[j]/i-1
                        elif l[j]>i:
                                s+=l[j]/i
                        j+=1
                ans=min(ans,s)
                i+=1
        fp.write('Case #%d: %s\n' %(_,ans))
fp.close()
