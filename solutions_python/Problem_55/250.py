import sys


cases=int(sys.stdin.readline())

for i in range(1, cases+1):
    [r, k, n]=sys.stdin.readline().split()
    n=int(n)
    k=int(k)
    r=int(r)
    g=map(int, sys.stdin.readline().split())
    o=[]
    for j in range (len(g)):
        groups=0
        places=k
        while(places-g[(j+groups)%len(g)]>= 0 and groups < len(g)):
            places-=g[(j+groups)%len(g)]
            groups+=1
        o.append(((k-places), (j+groups)%len(g)))
#    print o
    money=0
    location=0
    for k in range(r):
#        print location
        (m, location)=o[location]
        money+=m
    print "Case #%d: %d"%(i, money)
        
