       
t = input()
for i in xrange(t):
    n = input()
    a = map(int,raw_input().split())
    ans = 9999999999

    x = 1
    while x<=1000:
        y = x
        z = 0
        while z<len(a):
            y+=(a[z]-1)/x
            z+=1
        x+=1
        ans = min(ans,y)
    
        
    
    s = "Case #%d: %d"%(i+1,ans)
    print s
