f=open("A-small-attempt0.in", "r")
out=open("test.out", "w")

T=int(f.readline())

def compute(N, K):
    a=[False for i in range(N)]
    
    for i in range(K):
        p=0
        while a[p] and p<N-1:
            p+=1
        for i in range(p+1):
            a[i]=not a[i]
    
    res=True
    for i in a:
        if not i:
            res=False
    
    if res:
        return "ON"
    else:
        return "OFF"

for i in range(T):
    [n,k]=[int(x) for x in f.readline().split(" ")]
    print "Case #%d: %s" % (i+1,compute(n,k))
