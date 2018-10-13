
t = int(raw_input())  
for e in xrange(1, t + 1):
    
    x, k = [str(s) for s in raw_input().split(" ")]  
    x=list(x)
    k=int(k)

    count=0
    mark=False
    for i in range(0,len(x)-k+1):
        if x.count(x[0]) == len(x):
            if x[i]=='+':
                mark=True
                break
        
        if x[i]=='-':
            count=count+1
            j=i
            
            for l in range(k):
                
                if x[j]=='-':
                    x[j]='+'
                else:
                    x[j]='-'
                j=j+1
            
    if x.count(x[0]) == len(x):
            if x[i]=='+':
                mark=True
                

    if mark==True:
        
        print "Case #{}: {}".format(e, count)
    else:
               
        print "Case #{}: {} ".format(e,'IMPOSSIBLE' )
