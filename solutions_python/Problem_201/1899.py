t=int(raw_input())
output=[]

for a0 in xrange(t):
    n,k=map(int,raw_input().split())
    v=[n]
    while max(v)>0 and k!=0:
        c=max(v)
        i=v.index(c)
        if c%2==0:
            a=c/2
            b=a-1
        else :
            a=(c-1)/2
            b=a
        v[i]=a
        v.append(b)
        k=k-1
    output.append(str(a)+' '+str(b))
            
         
    
    
    
for a0 in xrange(t):
    print 'Case #'+str(a0+1)+': '+output[a0]
