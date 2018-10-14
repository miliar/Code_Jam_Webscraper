def fn():
    c,f,x = map(float,raw_input().split())
    r = 2
    t = 0
    mx = 100000
    for i in range(100001):
        tmp = x/r
        mx = min(tmp+t,mx)
        t+=(c/r)
        r+=f      
    return mx

t = int(raw_input())

for i in range(t):
    print "Case #"+str(i+1)+": "+str(fn())

