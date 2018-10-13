from  sys import stdin
import math
t = int(stdin.readline())
for ca in xrange(1,t+1):
    n,k = map(int,stdin.readline().split())
    a = []
    for i in xrange(n):
        x,y = map(int,stdin.readline().split())
        a.append((x,x*y,y))
    
    ans = 0 
    a.sort()
    a.reverse()
    #print a
    for i in xrange(n):
        cur = 0
        b = []
        for j in xrange(n):
            if j!=i:
                b.append(a[j][1])
            b.sort()
            b.reverse()
        cur = 2*sum(b[:k-1]) + a[i][1]*2            
        
        cur += a[i][0]**2
        #print "taking ",i,j,cur*math.pi
        ans = max(ans, cur)
    print  "Case #%d: %.10f"%(ca,ans*math.pi)       
        