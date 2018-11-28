def solve(S, K):
    count = 0
    S = [True if x=='+' else False for x in S]
    
    def flip(n):
        for i in xrange(n, K+n):
            if S[i]:
                S[i] = False
            else:
                S[i] = True  
                
    for i in xrange(len(S)-K+1):
        if not S[i]:
            flip(i)
            count += 1
    if False in S:
        return "IMPOSSIBLE"
    return count
            

        

for i in xrange(1, input()+1):
    l = raw_input().split()
    print "Case #%d: %s"%(i, solve(l[0], int(l[1])))