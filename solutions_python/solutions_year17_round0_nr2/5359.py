a=[]
l=int(input())
d=1
while(l!=0):
    
    n=str(input())
    c=[]
    a=[]
    
    for i in n:
        a.append(i)
        c.append(i)
    a.sort()
    if a==c:
        b="".join(a)
        print("Case #{}: {}".format(d,int(b)))
        d=d+1
    else:

    
         for i in range(len(c)-1):
             if c[i]>=c[i+1]:
                 c[i]=str(int(c[i])-1)
                 for j in range(i+1,len(c)):
                     c[j]='9'
                 break
    
            
         b="".join(c)
         print("Case #{}: {}".format(d,int(b)))
         d=d+1
    l=l-1;
