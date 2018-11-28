def f(s,k):
    n = len(s)
    v = [0]
    c = 0
    for i in range(n-k+1):
        v.append(v[max(0,i-k+1)]^(s[i]=='-'))
        c += (v[-1] != v[-2])
    for i in range(n-k+1,n):
        # i-k+1..i
        if (v[-1]^v[max(0,i-k+1)]) != (s[i]=='-'):
            return None
    return c

t = input()
for icase in range(1,t+1):
    s, k = raw_input().split()
    k = int(k)
    res = f(s,k)
    if res is None:
        print 'Case #%d: IMPOSSIBLE' % icase
    else:
        print 'Case #%d: %d' % (icase, res)
