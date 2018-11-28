def is_nondecreasing(n):
    S = map(int, str(N)[::-1])
    K = len(S)
    for i in xrange(K-1):
        if S[i] < S[i+1]:
            return False
    return True


prefix = "Case #%d:"
T = int(raw_input())
for t in xrange(1, T+1):
    N = int(raw_input())
    while not is_nondecreasing(N):
        S = map(int, str(N)[::-1])
        K = len(S)
        for i in xrange(K):
            if S[i] != 9:
                N -= (S[i]+1) * (10**i)
                break
        
    
    print prefix%t, N
