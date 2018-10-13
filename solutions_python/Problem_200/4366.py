t=int(raw_input())
p=[0]*t
for i in xrange(t):
    p[i]=int(raw_input())
    for j in xrange(p[i], 0, -1):
        s=str(j)
        lst=list(s)
        #print lst
        lst1=sorted(lst)
        #print lst1
        if lst==lst1:
            break
    
    print "Case #"+str(i+1)+": "+str(j)
