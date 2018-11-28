def a(xx):
    chekall=True
    for i in xx:
        if i =='-':
            chekall=False
            break
    return chekall
        
T=int(input())
for ii in range(1,T+1):
    s,k=input().strip().split(' ')
    k=int(k)
    y=list(s)
    rrr=a(y)
    i=0

    t=0
    while i<=len(y)-k:
        if y[i]=='-':
            t+=1
            checkall=False
            r=0
            while r<=k-1:
                if y[i+r]=='+':
                    
                    y[i+r]='-'
                else:
                    y[i+r]='+'
                #print(y)
                r+=1
            #print(y)
        i+=1
    
        
    if rrr==True:
        print('Case #{}: 0'.format(ii))
    else:
        
        stat=True
        for i in y:
            if i=='-':
                stat=False
                break
        if stat==False:
            print('Case #{}: IMPOSSIBLE'.format(ii))
        else:
            print('Case #{}:'.format(ii),t)
        
        
            
