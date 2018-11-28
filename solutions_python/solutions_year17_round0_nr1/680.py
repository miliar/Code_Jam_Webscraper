import sys

T=int(sys.stdin.readline().strip())

for k in range(T):
    S, K = sys.stdin.readline().split(" ")
    K = int(K.strip())

    S = [(0 if c == '+' else 1) for c in S]
    
    j = 0
    for i in range(len(S) - K + 1):
        if S[i] == 0:
            continue

        j += 1
        for m in range(K):
            S[i+m] = 1 - S[i+m]

    if sum(S) > 0:
        print("Case #%d: IMPOSSIBLE" % (k + 1))
    else:
        print("Case #%d: %d" % (k + 1, j))
        
