def f(s):
    n = len(s)
    i = 1
    while i < n and s[i] >= s[i-1]:
        i += 1
    if i == n:
        return s
    i -= 1
    while i > 0 and s[i-1] == s[i]:
        i -= 1
    o = s[:i] + str(int(s[i])-1) + '9' * (n-i-1)
    return o.lstrip('0')

t = input()
for icase in range(1,t+1):
    s = raw_input().strip()
    print 'Case #%d: %s' % (icase, f(s))
