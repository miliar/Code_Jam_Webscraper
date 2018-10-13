T = int(input())
for i in range(T):
    (S, K) = input().split()
    S = list(S)
    K = int(K)
    count = 0
    for j in range(len(S)-K+1):
        if S[j] == '-':
            for k in range(K):
                if S[j+k] == '-':
                    S[j+k] = '+'
                elif S[j+k] == '+':
                    S[j+k] = '-'
            count += 1
    count = str(count)
    for j in range(len(S)):
        if S[j] == '-':
            count = 'IMPOSSIBLE'
    print('Case #%d: %s' % (i+1, count))
