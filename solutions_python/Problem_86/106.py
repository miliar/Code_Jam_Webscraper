
def Solve(L, H, freq):
    
    for f in range(L, H+1):
        allgood = True
        for otherfreq in freq:
            if otherfreq % f != 0 and f % otherfreq != 0:
                #print "no good:", f, otherfreq
                allgood = False
                break
        if allgood:
            return f
    return "NO"
        
        




f = open('b.in')

T = int(f.readline())
for t in range(T):
    N, L, H = map(int, f.readline().split())
    freq = map(int, f.readline().split())
    #print freq
    result = Solve(L, H, freq)
    print "Case #%d: %s" % (t+1, result)