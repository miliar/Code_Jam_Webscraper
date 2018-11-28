n=int(raw_input())
for i in xrange(n):
    count=0
    d,n=map(float, raw_input().strip().split(' '))
    n=int(n)
    for j in range(1,n+1):
        p,s=map(float, raw_input().strip().split(' '))
        l=(d-p)/s
        if l>count:
            count=l
    print "Case #"+str(i+1)+": "+str(d/count)      
