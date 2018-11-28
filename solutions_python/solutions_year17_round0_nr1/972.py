T = input()
for _ in xrange(1, T + 1):
    s, k = raw_input().split(' ')
    k = int(k)
    ans = 0
    for i in xrange(len(s) - k + 1):
        if s[i] == '-':
            s = s[:i] + ''.join('-' if j == '+' else '+' for j in s[i:i + k]) + ('' if i + k > len(s) else s[i + k:])
            ans += 1
    print 'Case #%d: %s' % (_, 'IMPOSSIBLE' if '-' in s else str(ans))
