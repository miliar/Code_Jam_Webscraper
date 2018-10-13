T = int(raw_input().strip())

for t in range(T):
    S, K = raw_input().strip().split()
    K = int(K)
    S = [c for c in S]
    
    i = 0
    count = 0
    while i <= len(S) - K:
        if S[i] == '-':
            for j in range(K):
                if S[i + j] == '+':
                    S[i + j] = '-'
                else:
                    S[i + j] = '+'
            count += 1
        i += 1

    is_possible = all([c == '+' for c in S[i:]])
    if is_possible:
        print('Case #{:d}: {:d}'.format(t + 1, count))
    else:
        print('Case #{:d}: IMPOSSIBLE'.format(t + 1))

