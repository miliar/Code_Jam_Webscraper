def check(n):
    s=n%10;
    if(s==0):
        n=n-1;
        
    if(int(n/10)==0):
        return n;
    s=n%10;
    m=n;
    ml=0
    t=1
    n=int(n/10)
    while(n):
        p=n%10;
        if(p>s):
            ml=t
        
             
        s=p;
        n=int(n/10)    
        t=t+1
    n=m;
    if(ml):
        aq=0
        ss=ml
        while(ss):
            aq=aq*10+9
            ss=ss-1
        n=int(m/10**ml)
        n=n-1;
        n=n*10**ml+aq
    return n

t = int(input())  
for i in range(1, t+1):
   m = int(input())
   w=18
   while(w):
    m=check(m)
    w=w-1;   
   print("Case #{}: {}".format(i,m ))
  
