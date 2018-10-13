T = int(raw_input())
for i in range(T):
    Smax,S = raw_input().split()
    Smax = int(Smax)
    acc = 0
    result = 0
    for j in range(Smax+1):
        s = int(S[j])
        if acc < j:
            d = j - acc
            result += d
            acc += d
        acc += s
    print "Case #%d: %d"%(i+1,result)

