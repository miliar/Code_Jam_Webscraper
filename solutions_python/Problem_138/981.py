t = int(raw_input())
m = t
while(t) :
    n = int(raw_input())
    s1 = raw_input()
    s2 = raw_input()
    l1 = s1.split(' ')
    l2 = s2.split(' ')
    for x in range(0,n) :
        l1[x] = float(l1[x])
        l2[x] = float(l2[x])
    l1.sort()
    l2.sort()
    nw,ndw,kw = 0,0,0
    j = 0
    for i in range(0,n) :
        if(l1[i]>l2[j]) :
            j+=1
            ndw+=1
            #print ndw
    j = 0
    for i in range(0,n) :
        if(l2[i]>l1[j]) :
            j+=1
            kw+=1
            #print kw
    nw = n-kw
    print 'Case #%d: %d %d'%(m-t+1,ndw,nw)
    t-=1


        
    
    
