
def solve(f):
    R, k, _ = map(int, f.readline().split())
    G = map(int, f.readline().split())
   
    money = 0
    for ride in xrange(R):
        riders = 0
        for g in xrange(len(G)):
            if riders+G[g] <= k:
                riders += G[g]
            else:
                break
        money += riders
        G = G[g:] + G[:g]
        
    return money        
   

with open('C-small.in', 'r') as f:
    T = int(f.readline())
    results = [solve(f) for i in xrange(T) ]
    for i in xrange(T):
        print "Case #%d: %s" % (i+1, results[i])