def isTidy(X):
    a=[]
    while X!=0:
        a.append(X%10)
        X/=10
    flag=0
    for i in range(0,len(a)-1):
        if a[i]<a[i+1]:
            flag=1
            break
    return False if (flag==1) else True
T=int(raw_input().strip())
for i in range(1,T+1):
    N=int(raw_input().strip())
    b=N
    a=[]
    while b!=0:
            a.append(b%10)
            b=b/10
    if(not isTidy(N)):
        N=N-(a[0]+1)
        b=N
        a=[]
        while b!=0:
            a.append(b%10)
            b=b/10
        for key in range(1,len(a)-1):
            flag1=0
            #print N
            for naina in range(key+1,len(a)):
                if a[key]<a[naina]:
                    flag1=1
                    break
            if flag1==1:
                N=N-(a[key]+1)*(10**key)
                
            b=N
            a=[]
            while b!=0:
                a.append(b%10)
                b=b/10
            
    print "Case #%d: %d"%(i,N)
   
