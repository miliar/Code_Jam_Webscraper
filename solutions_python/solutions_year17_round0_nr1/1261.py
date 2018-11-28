for t in range(int(input())):
    s, k = input().split()
    s = [1 if c=='+' else 0 for c in s]
    k = int(k)
    flips = 0
    for i in range(len(s)-k+1):
        if s[i]==0:
            flips += 1
            for j in range(i, i+k):
                s[j] ^= 1
    for i in range(len(s)-k+1, len(s)):
        if s[i]==0:
            flips = 'IMPOSSIBLE'
            break

    print('Case #{}: {}'.format(t+1, flips))