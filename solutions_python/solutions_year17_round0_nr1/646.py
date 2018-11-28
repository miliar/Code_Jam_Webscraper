T = int(raw_input())
for ii in range(T):
    S,K = raw_input().split()
    S = map(lambda x: 1 if x=='+' else 0, S)
    K = int(K)
    f = 0
    for i in range(len(S)-K+1):
        if not S[i]:
            S[i:i+K] = map( lambda x: 0 if x else 1, S[i:i+K])
            f+=1
    r = f
    if 0 in S[-K:]:
        r = 'IMPOSSIBLE'
    print 'Case #'+str(ii+1)+':'+' '+str(r)
            