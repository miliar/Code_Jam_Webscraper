t = int(raw_input())  # read a line with a single integer
for numtest in xrange(1, t + 1):
    r,c=[int(k) for k in raw_input().split(" ")]    
    nbl=0
    d={}
    for i in range(r): 
        mi=raw_input()
        d[i]=[mi[k] for k in range(c)]
        nbl+=len([k for k in d[i] if k=="?"])
 #   while nbl>0:
    for i in range(r):
        for j in range(1,c):
            if d[i][j]=="?" and d[i][j-1]!="?":
                d[i][j]=d[i][j-1]
                nbl-=1
        for j in range(c-2,-1,-1):
            if d[i][j]=="?" and d[i][j+1]!="?":
                d[i][j]=d[i][j+1]
                nbl-=1
             
#    for i in range(r):
#        resi=""
#        for j in range(c):
#            resi+=d[i][j]
#        print "{}".format(resi)
#        
        #now empty lines
    for i in range(1,r):
        if d[i][0]=="?" and d[i-1][0]!="?":
            for j in range(c):
                d[i][j]=d[i-1][j]
                nbl-=1
    for i in range(r-2,-1,-1):
        if d[i][0]=="?" and d[i+1][0]!="?":
            for j in range(c):
                d[i][j]=d[i+1][j]
                nbl-=1
    
    if nbl!=0:
        print "euh"
        1/0
                
    print "Case #{}:".format(numtest)
    for i in range(r):
        resi=""
        for j in range(c):
            resi+=d[i][j]
        print "{}".format(resi)
        
