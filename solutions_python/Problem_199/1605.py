T  = int(input())
for n in range(T):
    S = input().strip().split(' ')
    S, K = S[0], int(S[1])
    qnt = None
    if '-' not in S:
        qnt = 0
    else:
        qnt = 0
        while (len(S) >= K):
            while len(S) > 0 and ('+' not in S[:K] or '+' not in S[-1*K:] or '+' in S[0] or '+' in S[-1]):
                if len(S) >= K and '+' not in S[:K]:
                    S = S[K:]
                    qnt += 1
                elif len(S) >= K and '+' not in S[-1*K:]:
                    S = S[:-1*K]
                    qnt += 1
                elif '+' in S[0]:
                    S = S[1:]
                elif '+' in S[-1]:
                    S = S[:-1]
                if len(S) < K and len(S) > 0 and '+' not in S:
                    qnt = 'IMPOSSIBLE'
                    break
            if len(S) >= K:
                qnt += 1
                for i in range(K):
                    if S[i] == '+':
                        S = S[:i] + '-' + S[i+1:]
                    else:
                        S = S[:i] + '+' + S[i+1:]
        if len(S) > 0:
            qnt = 'IMPOSSIBLE'
    print("Case #{}: {}".format(n+1, qnt))
