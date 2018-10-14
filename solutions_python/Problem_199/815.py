def flip(s, i, k):
    for j in range(i, i+k):
        s[j] = '+' if s[j] == '-' else '-'

n = int(input())
for q in range(n):
    s, k = input().split()
    s = list(s)
    k = int(k)
    n = len(s)

    c = 0
    for i in range(len(s)):
        if s[i] == '-' and i + k <= n:
            flip(s, i, k)
            c += 1
    if any(s[i] == '-' for i in range(n)):
        c = 'IMPOSSIBLE'

    print("Case #{}: {}".format(q+1, c))
