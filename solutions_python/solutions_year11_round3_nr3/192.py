def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def lcm(a,b):
    return a*b/gcd(a,b)

def lcm_l(l):
    return reduce(lcm,l)

def find_best(otherfreq,L,H):
    """find a number in range L..H which divides every number in otherfreq"""
    for x in range(L,H+1):
        done=True
        for y in otherfreq:
            if(not (x%y==0 or y%x==0)):
                done=False
                break
        if(done):
            return x
    return -1
    
    """if(len(otherfreq)==0):
        return -1
    c = lcm_l(otherfreq)
    if(c>=L and c<=H):
        return c
    else:
        return find_best(otherfreq[:-1],L,H)"""

def best_freq(L,H,otherfreq):
    if(L<=1):
        return 1
    return find_best(otherfreq,L,H)
    
        
    

T = int(raw_input())
for tc in range(T):
    N,L,H = [int(x) for x in raw_input().split()]
    otherfreq = [int(x) for x in raw_input().split()]
    best = best_freq(L,H,otherfreq)
    print "Case #%d: "%(tc+1),
    if best==-1:
        print "NO"
    else:
        print best
    
    
    
