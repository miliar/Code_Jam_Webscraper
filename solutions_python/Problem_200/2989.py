t = input()

def ans(n):
    k = map(int,list(str(n)))
    i = 0
    while i<len(k)-1:
        if k[i]>k[i+1]:
            k[i]-=1
            j = i+1
            while j<len(k):
                k[j] = 9
                j+=1
            i = -1
            
        
        i+=1
    s = 0
    c = len(k)-1
    for i in xrange(len(k)):
        s+=k[i]*(10**c)
        c-=1
    return s
			


for i in xrange(t):
    n = input()
    
    #print i
    
    s = 'Case #%d: %d'%(i+1,ans(n))
    print s
    
