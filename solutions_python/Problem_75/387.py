from collections import defaultdict
n=input()

for case in range(n):
    res=[]
    data = iter(raw_input().split())
    c=[next(data) for i in range(int(next(data)))]
    C=dict((i+j, k) for i,j,k in c)
    C.update(dict((j+i, k) for i,j,k in c))
    D=set(next(data) for i in range(int(next(data))))
    next(data)
    N=next(data)
    
    for n in N:
        if res and res[-1]+n in C:
            n=C[res[-1]+n]
            res[-1:] = []
        for i in res:
            if i+n in D or n+i in D:
                res=[] 
                break
        else:
            res.append(n)
        
    
    print "Case #%s:"%(case+1), repr(res).replace("'","")
