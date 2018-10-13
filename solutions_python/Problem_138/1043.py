
def solve(test):
    n= int(raw_input())
    naomis =[ float(f) for f in raw_input().split() ]
    kens = [ float(f) for f in raw_input().split() ]
    naomis.sort()
    kens.sort()
    l=[]
    k=[]
    i=0
    j=0
    pres=0
    for i in xrange(n):
        while j<n and (naomis[i]>kens[j]) :
            k.append(i)
            j+=1
        l.append(j)
    i+=1
    while j<n:
        k.append(i)
        j+=1
    # print naomis
    # print kens
    # print l,k    
    count1=0
    count2=0
    t1=n
    t2=n




    for i in xrange(n-1,-1,-1):
        if l[i]!=0 and t1>0:
            count1+=1
            if t1>l[i]:
                t1=l[i]-1
            else:
                t1-=1
            # print "count , temp",count1, t1
        # print i
        if k[i]!=0 and t2!=0:
            # print count2, i, t2
            count2+=1
            if t2>k[i]:
                t2=k[i]-1
            else:
                t2-=1
            # print "count , temp",count2, t2


    print "Case #%d: %d %d"%(test,count1,n-count2)
    




    

    




    


t = int(raw_input())
for i in xrange(t):
    solve(i + 1)
