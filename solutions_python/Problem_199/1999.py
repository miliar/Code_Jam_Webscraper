for t in range(int(input())):
    s, k = input().split()
    s, k, v = [si == '+' for si in s], int(k), 0
    for i in range(len(s) - k + 1):
        if not s[i]:
            for j in range(i, i + k):
                s[j] = not s[j]
            v += 1
    print('Case #{}: {}'.format(t + 1, v if all(s) else 'IMPOSSIBLE'))
