t = int(raw_input())

for i in xrange(t):
    s,k = raw_input().split(' ')
    k = int(k)
    s = list(s)
    l = len(s)
    ans = 0
    for j in xrange(l-k+1):
        if s[j] == '-':
            ans += 1
            for x in xrange(k):
                s[j+x] = '+' if s[j+x] == '-' else '-'
    if '-' in s:
        print 'Case #{0}: IMPOSSIBLE'.format(i+1)
    else:
        print 'Case #{0}: {1}'.format(i+1, ans)
 