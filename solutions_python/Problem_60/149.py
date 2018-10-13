import sys
f = open(sys.argv[1], "rt")
T =  int(f.next().strip())
for t in range(T):
        N, K, B, T = map(int, f.next().strip().split())
        X = reversed(map(int, f.next().strip().split()))
        V = reversed(map(int, f.next().strip().split()))
        switches = 0
        got = 0
        reqs = 0
        for x, v in zip(X, V):
            if T*v+x < B: switches = switches + 1
            else: 
                reqs += switches
                got += 1
                if got == K: break
        if got == K: print 'Case #%d: %d' %(t+1, reqs)
        else: print 'Case #%d: IMPOSSIBLE' %(t+1)
                    
                
        

