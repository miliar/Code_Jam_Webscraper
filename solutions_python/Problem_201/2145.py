
T = int(raw_input())

for i in range(T):
    r = raw_input().split()
    #r = ["10000","1000"]
    n = int(r[0])
    k = int(r[1])
    
    b = [None for qq in range(n)]
    
    for j in range(k):
        maxl = 0
        maxr = -1
        
        l = 0
        while l<n and b[l]==1:
            l+=1
        r = l
        
        while l<n:
            
            while r+1<n and b[r+1]==None:
                r += 1
            
            if r-l>maxr-maxl:
                maxr,maxl = r,l
            
            l = r + 1
            while l<n and b[l]==1:
                l+=1
            r = l
        
        b[(maxl+maxr)/2] = 1
        #print b
        
        if j ==k-1:
            l,r = maxl,maxr
            print "Case #"+str(i+1)+":",r-(l+r)/2, (l+r)/2-l
        
        
    
    
    
    
    
    
    
    
    
    