T = int(input())
for t in range(T):
    sK = raw_input().split()
    s, K = list(sK[0]), int(sK[1])
    possible = True
    n_flips = 0
    for i in range(len(s)):
        c = s[i]
        if c != '+':
            if i + K > len(s):
                possible = False
                break
            n_flips += 1
            for k in range(K):
                s[i+k] = '+' if s[i+k] == '-' else '-'
    w = str(n_flips) if possible else 'IMPOSSIBLE'
    print('Case #{}: {}'.format(t+1, w))
