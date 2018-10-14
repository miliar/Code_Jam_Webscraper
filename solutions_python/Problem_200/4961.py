def tidy(n):
    m=n%10
    n/=10
    while(n>0):
        d=n%10
        if(d>m):
            return False
        else:
            m=d
        n/=10
    return True
        
f = open("B-small-attempt0.in", "r") 
t = int(f.readline())
for i in range(t):
    n = int(f.readline())
    for j in xrange(n,0,-1):
        if(tidy(j)):
            print("Case #"+str(i+1)+": "+str(j))
            break
f.close() 
