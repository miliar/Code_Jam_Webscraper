n = int(input())

for test in range(1, n + 1):
    s, k = input().split()
    s = list(s)
    k = int(k)

    ans = 0
    for i in range(len(s) - k + 1):
        if s[i] == '-':
            ans += 1
            for j in range(k):
                s[i + j] = '+' if s[i + j] == '-' else '-'

    if ''.join(s) == '+' * len(s):
        print('Case #%d: %d' % (test, ans))
    else:
        print('Case #%d: IMPOSSIBLE' % test)
