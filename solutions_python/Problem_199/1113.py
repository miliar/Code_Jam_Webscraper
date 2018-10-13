T = input()
for t in range(T):
    S, K = raw_input().split()
    S = list(S)
    K = int(K)

    turns = 0
    for i in range(len(S)-K+1):
        if S[i]=='-':
            turns += 1
            for j in range(K):
                S[i+j] = '-+'[S[i+j]=='-']

    if S.count('-'):
        turns = 'IMPOSSIBLE'
    else:
        turns = str(turns)

    print "Case #%d: %s"%(t+1, turns)
