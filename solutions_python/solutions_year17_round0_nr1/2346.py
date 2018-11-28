for t in range(int(input())):
    S, K = input().split()
    S = [True if x is '+' else False for x in S]
    K = int(K)

    y = 0
    for i, s in enumerate(S):
        if not s and i <= len(S) - K:
            y += 1
            for j in range(i, i+K):
                S[j] = not S[j]

    if False in S:
        print(f'Case #{t+1}: IMPOSSIBLE')
    else:
        print(f'Case #{t+1}: {y}')
