def conv(c):
    if c == '-':
        return 1
    else:
       return 0

def sol(s,k):
    t = [conv(c) for c in s]
    n = len(s)
    u = [9 for i in range(n-k+1)]
    for i in range(min(n-k+1,k)):
        u[i] = abs((t[i] + sum([u[j] for j in range(max(0,i-k+1),i)])) % 2)       
    for i in range(n-k,min(n-k,k-1),-1):
        u[i] = abs((t[i+k-1] + sum([u[j] for j in range(i+1,min(n-k+1,i+k))])) % 2)
    for i in range(n):
        tx = abs(( sum([u[j] for j in range(max(0,i-k+1),min(n-k+1,i+1) )  ]) ) % 2)
        
        if tx != t[i]:
            return "IMPOSSIBLE"
    return sum(u)


t = int(raw_input().strip())
for a0 in xrange(t):
    r = raw_input().strip().split(" ")
    s = r[0]
    k = int(r[1])
    print "Case #%d: %s" % (a0+1,sol(s,k))

