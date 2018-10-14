t=int(raw_input())
output=[]

for a0 in xrange(t):
    n=raw_input()
    v=list(n)
    c=len(v)
    i=0
    while i<c-1 and i>=0:
        if v[i]>v[i+1]:
            v[i]=str(int(v[i])-1)
            j=i
            v=v[:i+1]+list('9'*(c-i-1))
            i=i-1
        else :
            i=i+1
            
        
    
        
    output.append(str(int(''.join(v))))
         
    
    
    
for a0 in xrange(t):
    print 'Case #'+str(a0+1)+': '+output[a0]
