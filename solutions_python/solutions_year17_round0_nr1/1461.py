T = int(input())
for t in range(T):
    S, K = [i for i in input().split(" ")]
    S = list(S)
    K = int(K)
    i = 0
    flips = 0
    while i <= len(S) - K:
        if S[i] == '-':
            for j in range(i, i + K):
                if S[j] == '+':
                    S[j] = '-'
                else:
                    S[j] = '+'
            flips += 1
        i += 1
    possible = True
    for x in range(i, len(S)):
        if S[x] == '-':
            possible = False
            break
    if possible:
        print('Case #{}: {}'.format(t + 1, flips))
    else:
        print('Case #{}: {}'.format(t + 1, "IMPOSSIBLE"))