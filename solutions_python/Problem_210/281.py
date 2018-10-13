from sys import stdin
t = int(stdin.readline())
def di(x,y):
    ans = y-x
    ans %= 1440
    if ans < 0:
        ans += 1440
    return ans        
for ca in xrange(1,t+1):
    n,m = map(int,stdin.readline().split())
    a = []
    b = []
    for i in xrange(n):
        x,y = map(int,stdin.readline().split())
        a.append((x,y))
    for i in xrange(m):
        x,y = map(int,stdin.readline().split())
        b.append((x,y))
    a.sort()
    b.sort()
    
    ans = 2
    if n==2 or m==2:
        c = a+b
        c.sort()
        x1,y1 = c[0]
        x2,y2 = c[1]
        #print x1,y1,x2,y2,di(x1,y2),di(x2,y1)
        if di(x1,y2) > 720 and di(x2,y1)>720:
            ans = 4
    print "Case #%d: %d"%(ca,ans)        