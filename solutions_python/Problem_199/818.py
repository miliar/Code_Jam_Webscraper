num_cases = int(input())
for c in range(num_cases):
    S, K = input().split(' ')
    S = [s == '+' for s in S]
    K = int(K)
    flips = 0
    for i in range(len(S) - K + 1):
        if not S[i]:
            flips += 1
            for j in range(i, i + K):
                S[j] = not S[j]
    for i in range(len(S) - K + 1, len(S)):
        if not S[i]:
            flips = 'IMPOSSIBLE'
    print('Case #{}: {}'.format(c + 1, flips))
