from fractions import gcd

def FairWarning(N, T, u):
##    T.sort()
##    g = T[0]
##    for i in range(1, N):
##        g = gcd(g,T[i])
##    if g == T[0]:
##        return "Case #%d: %d\n" % (u, 0)
    tb = []
    
    for i in range(0,N-1):
        tb.append( abs(T[i+1]-T[i] ) )
    tb.sort()
    i = 0
    while i<len(tb) and tb[i] == 0:
        i += 1
    if i>=len(tb):
        g = 0
    else:
        g = tb[i]
        for j in range(i,len(tb)):
            g = gcd(g,tb[j])
    if g == 1:
        output = 0
    elif g == 0:
        output = T[0]
    else:
        if T[0]%g == 0:
            output = 0
        else:
            output = g - T[0]%g
    return "Case #%d: %d\n" % (u, output)


fp = open("B-large.in", 'r')
fout = open("B-large.out", 'w')
T = int(fp.readline())
for i in range(1, T+1):
    tmp = fp.readline().split()
    N = int(tmp[0])
    t = []
    for j in range(1, len(tmp)):
        t.append( int(tmp[j]) )
    fout.write(FairWarning(N, t, i))
fp.close()
fout.close()
