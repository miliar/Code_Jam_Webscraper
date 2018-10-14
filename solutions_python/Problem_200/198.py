t = int(raw_input())
for x in xrange(t):
    n = list(map(int, raw_input().replace('\r', '')))
    for i in reversed(xrange(1, len(n))):
        if not(n[i-1] <= n[i]):
            n = n[:i-1] + [n[i-1]-1] + [9 for _ in xrange(len(n)-i)]
    print 'Case #{}: {}'.format(x+1, int(''.join(map(str, n))))