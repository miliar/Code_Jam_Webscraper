import sys

t=int(input().strip())
for i in range(t):
    n=int(input().strip())
    x=[]
    x=str(n)
    c=[]
    for digits in x:
        c.append(int(digits))   
    b=len(c)
    y=len(c)
    b=b-1
    t=""
    while b>0:
        if c[b]<c[b-1]:
            c[b-1]=c[b-1]-1
            j=b
            while(j<y):
                c[j]=9
                j=j+1
        b=b-1

    p=0
    if c[p]==0:
        p=p+1
        
    while p<y:
        t=t+str(c[p])
        p=p+1
    print("Case #"+str(i+1)+": "+t)    
    
    
