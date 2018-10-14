def flip(x):
    return '-' if x == '+' else '+'

T = int(raw_input())
for case in range(T):
    S, K = raw_input().split()
    K = int(K)
    S = list(S)
    N = len(S)

    target = '+'
    flips = 0
    success = True
    
    for i in range(N-(K-1)):
        if S[i] != target:
            for j in range(i, i+K):
                S[j] = flip(S[j])
            flips += 1

    for i in range(N-(K-1), N):
        if S[i] != target:
            success = False
            break
    
    ans = str(flips) if success else 'IMPOSSIBLE'
    print 'Case #%d: %s' % (case+1, ans)
