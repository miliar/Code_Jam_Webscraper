t=int(raw_input(''))
for a0 in xrange(t):
    q=raw_input('')
    
    list1= map(int, q.split())
    d= list1[0]
    n= list1[1]
    dist=0
    tim=0
    fintim=0
    
    for i in xrange(n):
        a=raw_input('')
        e= map(int, a.split())
        f= e[0]
        k= e[1]
    
        
        dist=d-f
        tim=float(dist)/float(k)
        if tim>fintim:
            fintim=tim
       
    ans=float(d)/float(fintim)
    print "Case #"+str(int(a0+1))+":",'%.6f' % ans
        
