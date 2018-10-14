t = int(raw_input())

for a0 in range(1, t+1):
    s, k = raw_input().strip().split()
    s = list(s)
    k = int(k)

    n = len(s)

    a = [True for i in range(n)]

    for i in range(n):
        if s[i] == '-':
            a[i] = False

    i = 0

    ans = 0

    while (i < n-k+1):
        if a[i] == 0:
            for j in range(i, i+k):
                a[j] = not a[j]
            ans += 1
        i += 1

    for i in range(n-k+1, n):
        if a[i] == False:
            ans = 'IMPOSSIBLE'
            break

    print 'Case #{}: {}'.format(a0, ans)

