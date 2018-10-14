t=int(input())
r=[]
for i in range(t):
    n=int(input())
    for j in range(n,-1,-1):
        b=str(j)
        dobar=True
        for k in range(len(b)-1):
            if b[k]>b[k+1]:
                dobar=False
                break
        if dobar:
            r.append(j)
            break
        
for i in range(len(r)):
    print('Case #',i+1,':',' ',r[i],sep='')        
                
    