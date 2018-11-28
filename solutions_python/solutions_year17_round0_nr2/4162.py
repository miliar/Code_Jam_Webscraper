#!/usr/bin/python
T=int(raw_input())
i=1
while i!=T+1:
    a=raw_input()
    b=all(c<=d for c,d in zip(a,a[1:])) 
    print 'Case #%d:'%i,
    if b:
        print a
    else:
        j=0
        while j!=len(a):
            if int(a[j])>int(a[j+1]):
                z=j
                break
            j+=1
        v=a.index(a[z])
        l=map(int,a)
        m=l[:v]
        m=map(str,m)
        n=l[v]
        o=l[v+1:]
        n=str(n-1)
        p='9'*len(o)
        print int(''.join(m)+n+p)
    i+=1
    
    
            
            
            
    
    






































