T = int(raw_input())

for i in range(T):
    S, K = raw_input().split()
    S = [s for s in S]
    K = int(K)
    flips = 0
    for j in range(len(S)-K+1):
        if S[j] == '-':
            flips += 1
            for f in range(j, j+K):
                S[f] = '+' if S[f] == '-' else '-'
    if any([x == '-' for x in S]):
        print "Case #{0}: IMPOSSIBLE".format(i+1)
    else:
        print "Case #{0}: {1}".format(i+1, flips)

