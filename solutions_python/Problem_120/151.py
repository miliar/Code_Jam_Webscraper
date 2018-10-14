def testmid(mid, r, t):
    if(mid * (2 * r + 1) + 2 * mid * (mid - 1) <= t):
        return True
    return False
        
def bsearch(lo, hi, r, t):
    while hi - lo > 1:
        mid = (lo + hi) / 2
        if(testmid(mid, r, t)):
            lo = mid
        else:
            hi = mid - 1
    if(testmid(hi, r, t)):
        return hi
    return lo
        
T = int(raw_input())
cnt = 1
while T > 0: 
    sp = raw_input().split(" ")
    r = int(sp[0])
    t = int(sp[1])
    print "Case #" + str(cnt) + ": " + str(bsearch(0,t, r, t))
    cnt = cnt + 1
    T = T - 1
