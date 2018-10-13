def solve(n, k):
    a = [(i, i, n-i-1) for i in range(n)]
    sort_func = lambda t: (min(t[1], t[2]), max(t[1], t[2]), t[0])
    
    for i in xrange(k):
        a.sort(key=sort_func)
        if False and k<10:
            print a
        winner = a[-1]
        ndx = winner[0]
        a.pop()
        for i in xrange(len(a)):
            p, L, R = a[i]
            if ndx<=p and ndx>=p-L:
                a[i] = (p, p-ndx-1, R)
            elif ndx>=p and ndx<=p+R:
                a[i] = (p, L, ndx-p-1)
    
    return winner[1], winner[2]

def fast_solve(n, k):
    i = s = 0
    while k - s -2**i > 0:
        s += 2**i
        i += 1
        
    # k-s >0
    n -= s
    k -= s
    
    #print "n-s=%d 2**i=%d k=%d" % (n, 2**i, k)
    if k<=n%(2**i):
        l = n/2**i+1
    else:
        l = n/2**i

    #print l
    if l>1:
        if l%2==0:
            return l/2, l/2-1
        else:
            return l/2, l/2
    else:
        return 0,0
        
    
    
#f = open("e:/work/code_jam/bathroom.txt", "r")
f = open("D:/downloads/C-large.in", "r")

T = int(f.readline())
for t in range(T):
    N, K = map(int, f.readline().split())
    sol = fast_solve(N, K)
    print "Case #%d: %d %d"  % (t+1, sol[0], sol[1]) 