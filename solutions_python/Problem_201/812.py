t=input()
def find(a):
    j=0
    k=0
    while k<a:
        k+=2**j
        j+=1
    return [k-2**(j-1),j-1]
def LsRs(a):
    if a%2==0:
        return [a/2,a/2-1]
    else:
        return [(a-1)/2,(a-1)/2]
for i in range(t):
    a=map(int,raw_input().split())
    stall=a[0]
    p=a[1]
    f=find(p)
    Ls=(stall-f[0])/(2**f[1])
    nummax=(stall-f[0])%(2**f[1])
    if p-f[0]<=nummax:
        ans=LsRs(Ls+1)
    else:
        ans=LsRs(Ls)
    print "Case #%d: %d %d" %(i+1,ans[0], ans[1])
    
