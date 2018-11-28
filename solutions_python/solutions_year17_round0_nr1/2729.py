T = int(input())

for i in range(T):
    S, K = input().split(' ')
    S = list(S)
    K = int(K)
    n_flips = 0
    for j in range(len(S[:-K])):
        c = S[j]
        if c == '-':
            n_flips += 1
            for k in range(K):
                S[j + k] = '+' if S[j + k] == '-' else '-'
    c = S[-K]
    for cc in S[-K+1:]:
        if cc != c:
            n_flips = 'IMPOSSIBLE'
    if isinstance(n_flips, int) and c == '-':
        n_flips += 1
    print('Case #' + str(i+1) + ': ' + str(n_flips))
