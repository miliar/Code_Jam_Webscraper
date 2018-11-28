from sys import stdin

T = int(stdin.readline().strip())


lines = []

for t in range(1,T+1):
    N, K = map(int, stdin.readline().strip().split())
    stalls = []

    n = 0
    while 1<<(n+1) <= K:
        n += 1
    p = 1<<n
    #print "P:", p
    base = (N)/p
    #print "Base:", base
    diff = N - base*p
    fake = (p - 1) - diff
    #print "Fake:", fake
    dist = base if K - (p - 1) <= p - fake else base -1
    #print dist
    
    L = dist/2 - 1 + (dist&1)
    R = dist/2
    
    # record the results
    lines.append("Case #%d: %d %d" % (t, R, L))
    print lines[-1]

with open('googjamc2.txt', 'w') as outfile:
    outfile.write("\n".join(lines))
