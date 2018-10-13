T = int(raw_input().strip())

for t in range(1, T + 1):
    s, k = raw_input().split()
    s = list(s)
    k = int(k)
    ans = 0
    for i in range(len(s) - k + 1):
        if s[i] == '-':
            ans += 1
            for j in range(i, i + k):
                if s[j] == '-':
                    s[j] = '+'
                else:
                    s[j] = '-'
    if any(c == '-' for c in s[-k:]):
        ans = 'IMPOSSIBLE'
    print 'Case #%s: %s' % (t, ans)
