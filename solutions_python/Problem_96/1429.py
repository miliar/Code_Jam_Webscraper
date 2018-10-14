T = int(raw_input())

for i in range(T):
    dat = map(int, raw_input().split())
    N = dat[0]
    S = dat[1]
    p = dat[2]
    t = dat[3:]
    
    ans = 0
    for v in t:
        if v < p: continue
        
        if v >= 3*p - 2:
            ans += 1
        elif v >= 3*p - 4 and S > 0:
            ans += 1
            S -= 1
    
    print "Case #%d: %s" % (i+1, ans)