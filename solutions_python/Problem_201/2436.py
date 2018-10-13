t=int(raw_input(''))
for q in xrange(t):
    x=raw_input('')
    d=map(int,x.split())
    n=d[0]
    k=d[1]
    arr=[]
    for i in xrange(2*k+1):
        arr.append(0)
    arr[0]=n
    u=0
    f=0
    
    for i in xrange(k):
        u=arr[i]
        if u%2==0:
            sec=(u/2)-1
            first=u/2
        else:
            first=u/2
            sec=first
        
        
        arr[(2*i)+1]=first
        arr[(2*i)+2]=sec
       
        
        
        arr=sorted(arr, reverse=True)
        
    
    print "Case #"+str(q+1)+":",max(first,sec),min(first,sec)