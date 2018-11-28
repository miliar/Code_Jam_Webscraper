for _ in range(int(input())):
    n,k=map(int,input().split())
    n+=2
    l=[(n-2-1)//2]
    r=[(n-2-1)-(l[0])]
    
    for i in range(k-1):
        c=max(max(l),max(r))
        if max(l)>max(r):
            l[l.index(c)]=((c-1)//2)
            r.append(c-1-((c-1)//2))
        else:
            l.append((c-1)//2)
            r[r.index(c)]=c-1-((c-1)//2)
    print("Case #%d: %d %d"%(_+1,max(min(l),min(r)),min(min(l),min(r))))

