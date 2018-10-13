import sys
T = int(sys.stdin.readline())
for t in range(T):
    (R, k, N) = map(int, sys.stdin.readline().split())
    G = map(int, sys.stdin.readline().split())
    #print R, k, N
    #print G
    answer = 0
    if len(G) == 1 and G[0] <= k:
        answer = G[0] * R    
    elif sum(G) <= k:
        answer = sum(G) * R
    else:
        for j in range(R):
            #print 'j = %d' %j
            if G[0] > k:
                break
            for i in range(2, len(G)+1):
                #print 'i=%d %d' %(i,len(G))
                #print 'k=%d, sum(G[:i])=%d' %(k , sum(G[:i]))
                
                if k < sum(G[:i]):
                    #print G, G[:i-1], sum(G[:i-1])
                    answer += sum(G[:i-1])
                    G = G[i-1:] + G[:i-1]
                    #print G
                    break
                #print 'test'
    print 'Case #%d: %d' %(t+1, answer)
                    
                
